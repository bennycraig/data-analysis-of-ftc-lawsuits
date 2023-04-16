import os
import json
import re
from pdfminer.high_level import extract_text


class WordCounter:
    def __init__(self, path_to_regex_json):
        self.word_count = {}
        self.num_words_in_case = 0 # Includes unmatches words
        self.context_of_words = ""

        # Open up JSON file containing regex search terms
        with open(path_to_regex_json) as f:
            self.re_prefix = json.load(f)

            # for category in self.re_prefix.keys():
            #     self.word_count[category] = {}

            #     for keyword in self.re_prefix[category].keys():
            #         self.word_count[category][keyword] = 0


    def read(self, text):
        self.num_words_in_case += len(text.split())

        for category in self.re_prefix.keys():
            for keyword in self.re_prefix[category].keys():
                pattern = fr"\b{self.re_prefix[category][keyword]}"

                matches = re.findall(pattern, text, flags=re.IGNORECASE)
                
                if len(matches) > 0: 
                    if category not in self.word_count:
                        self.word_count[category] = {}
                    if keyword not in self.word_count[category]:
                        self.word_count[category][keyword] = 0
                    self.word_count[category][keyword] += len(matches)

    def get_context(self, text):
        for category in self.word_count.keys():
            for keyword in self.word_count[category].keys():
                pattern = fr"\b{self.re_prefix[category][keyword]}"
                matches = re.finditer(pattern, text, flags=re.IGNORECASE)

                # If there are matches for keyword, print category & keyword
                one_match = re.search(pattern, text, flags=re.IGNORECASE)
                if one_match:
                    self.context_of_words += category + ": " + keyword + "\n"
                
                for match in matches:
                    start = max(0, match.start() - 5)
                    end = min(len(text), match.end() + 5)

                    # Find the beginning of the preceding word
                    if start > 0:
                        start_word = text.rfind(" ", 0, start) + 1  # the beginning of the preceding word
                    else:
                        start_word = 0  # the beginning of the text

                    # Find the end of the following word
                    end_word = text.find(" ", end)
                    if end_word < 0:
                        end_word = len(text)
                    
                    context = text[start_word:end_word]
                    context = context.replace("\n", "") # Remove newlines
                    self.context_of_words += context + "\n"

                if one_match:
                    self.context_of_words += "\n"

    def reset(self):
        self.num_words_in_case = 0

        for category in self.word_count.keys():
            for word in self.word_count[category].keys():
                self.word_count[category][word] = 0

        self.context_of_words = ""


    def save(self, dir):
        with open(os.path.join(dir, "word_count.json"), "w+") as f:
            out_dict = {}
            for category in self.word_count.keys():
                for word in self.word_count[category].keys():
                    if self.word_count[category][word] > 0:
                        if category not in out_dict:
                            out_dict[category] = {}
                        out_dict[category][word] = self.word_count[category][word]
            out_dict["NUM WORDS IN CASE"] = self.num_words_in_case

            json.dump(out_dict, f, indent=4)

        with open(os.path.join(dir, "context_of_words.txt"), "w+") as f:
            f.write(self.context_of_words)


def main():
    counter = WordCounter("searchTerms.json")

    root_dir = os.path.join("downloads_sample")

    with open("wordcount_log.txt", "w") as f:
        for industry in os.listdir(root_dir):
            industry_dir = os.path.join(root_dir, industry)
            if not os.path.isdir(industry_dir):
                continue

            for case in os.listdir(industry_dir):
                case_dir = os.path.join(industry_dir, case)
                if not os.path.isdir(case_dir):
                    continue

                for file in os.listdir(case_dir):
                    file_extension = os.path.splitext(file)[1]
                    if file_extension != ".pdf":
                        continue

                    file_path = os.path.join(case_dir, file)
                    
                    # Try-Except Block for broken PDFs
                    try:
                        text = extract_text(file_path)
                        counter.read(text)
                        counter.get_context(text)
                    except Exception as e:
                        print(f"Error processing {file_path}: {e}")
                        f.write(f"Error processing {file_path}: {e}\n")
                        continue

                counter.save(case_dir)
                print(f"Done with {case_dir}")
                f.write(f"Done with {case_dir}\n")

                counter.reset()


if __name__ == "__main__":
    main()