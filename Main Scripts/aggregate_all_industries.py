import os
import json

downloads_path = "downloads/"

# Initialize total_word_count and all_context
total_word_count = {"NUM WORDS": 0}
all_industries_word_count = {}
all_context = ""

# For each industry
for industry_folder in os.listdir(downloads_path):
    industry_path = os.path.join(downloads_path, industry_folder)

    # Check to make sure this is a folder (and not .DS_Store)
    if not os.path.isdir(industry_path):
        continue

    # AGGREGATE WORD COUNT FILE
    industry_word_count_file = os.path.join(industry_path, "industry_word_count.json")

    # Check if the industry_word_count.json file exists
    if os.path.exists(industry_word_count_file):
        
        # Open word count file for industry
        with open(industry_word_count_file, 'r') as f:
            industry_word_count = json.load(f)

        # Aggregate the word counts and the total number of words in the industry
        for topic, terms in industry_word_count.items():
            # Handle total number of words
            if topic == "NUM WORDS IN INDUSTRY":
                total_word_count['NUM WORDS'] += terms
            # Handle all other topics
            else:
                for term, count in terms.items():
                    if topic not in total_word_count:
                        total_word_count[topic] = {}
                    if term not in total_word_count[topic]:
                        total_word_count[topic][term] = 0
                    total_word_count[topic][term] += count

        # Add industry word counts to all_industries_word_count
        all_industries_word_count[industry_folder] = industry_word_count


    # AGGREGATE CONTEXT
    industry_context_file = os.path.join(industry_path, "industry_context.txt")

    if os.path.exists(industry_context_file):
        with open(industry_context_file, 'r') as f:
            industry_context = f.read()

        # Concatenate industry context to all_context
        all_context += f"\n=== INDUSTRY: {industry_folder} ===\n\n{industry_context}\n"

# Save the aggregated result as "total_word_count.json"
with open(os.path.join(downloads_path, "total_word_count.json"), 'w') as f:
    json.dump(total_word_count, f, indent=4)

# Save the aggregated context as "all_context.txt"
with open(os.path.join(downloads_path, "all_context.txt"), 'w') as f:
    f.write(all_context)

# Save the aggregated result as "all_industries_word_count.json"
with open(os.path.join(downloads_path, "all_industries_word_count.json"), 'w') as f:
    json.dump(all_industries_word_count, f, indent=4)