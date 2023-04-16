import os
import json

"""

Aggregate all word count files and context files into single files.

Loop through all cases in each industry and aggregate word counts into one file for
the industry. Also aggregates context files into one text file.


"""

downloads_path = "downloads/"

# For each industry
for industry_folder in os.listdir(downloads_path):
    
    # Initialize the industry word count
    industry_word_count = {"NUM WORDS IN INDUSTRY": 0}
    
    # Initialize industry context_of_words
    industry_context = ""

    industry_path = os.path.join(downloads_path, industry_folder)

    # Check to make this is a folder (and not .DS_Store)
    if not os.path.isdir(industry_path):
        continue

    # For each case in the industry
    for case_folder in os.listdir(industry_path):
        case_path = os.path.join(industry_path, case_folder)
        
        # Check to make this is a folder (and not .DS_Store)
        if not os.path.isdir(case_path):
            continue
        
        # AGGREGATE WORD COUNT FILE
        word_count_file = os.path.join(case_path, "word_count.json")
        
        # Check if the word_count.json file exists
        if os.path.exists(word_count_file):
            with open(word_count_file, 'r') as f:
                word_count = json.load(f)

            # Aggregate the word counts and the total number of words in the case
            for topic, terms in word_count.items():
                print("TOPIC:", topic, ":", terms)
                
                # Handle total number of words
                if topic == "NUM WORDS IN CASE":
                    industry_word_count['NUM WORDS IN INDUSTRY'] += terms
                # Handle all other topics
                else:
                    # For each term appearing in a topic
                    for term, count in terms.items():
                        if topic not in industry_word_count:
                            industry_word_count[topic] = {}
                        if term not in industry_word_count[topic]:
                            industry_word_count[topic][term] = 0
                        industry_word_count[topic][term] += count

        # AGGREGATE CONTEXT
        context_file = os.path.join(case_path, "context_of_words.txt")

        if os.path.exists(context_file):
            with open(context_file, 'r') as f:
                case_context = f.read()

            # Concatenate case context to industry context
            industry_context += f"\n--- {case_folder} ---\n\n{case_context}\n"

    # Save the aggregated result as "industry_word_count.json"
    with open(os.path.join(industry_path, "industry_word_count.json"), 'w') as f:
        json.dump(industry_word_count, f, indent=4)

    # Save the aggregated context as "industry_context_of_words.txt"
    with open(os.path.join(industry_path, "industry_context.txt"), 'w') as f:
        f.write(industry_context)
               