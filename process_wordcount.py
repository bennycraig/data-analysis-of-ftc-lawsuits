import json

""" 
This script reads in the all_industries_word_count.json file and processes it:
- Remove topics
- Normalize word counts by dividing by total words in industry

"""

# Read the data from the input JSON file
with open("all_industries_word_count.json", "r") as input_file:
    data = json.load(input_file)

keywords_to_remove = set([
    "biased algorithm",
    "biased data",
    "biodiversity",
    "biometric information privacy act",
    "board composition",
    "board diversity",
    "California Consumer Privacy Act",
    "child labor",
    "climate goal",
    "community impact",
    "company audits",
    "conflict mineral",
    "content moderation",
    "contract worker",
    "data bias",
    "differential privacy",
    "digital literacy",
    "diversity, equity and inclusion",
    "ethical supply chain",
    "extremist content",
    "false proxy",
    "harmful content",
    "labor condition",
    "management divesity",
    "marine resource",
    "market dominance",
    "misinformation",
    "misleading proxy",
    "online harassment",
    "platform responsibility",
    "platform worker",
    "racial harassment",
    "radicalization",
    "sexual harassment",
    "shareholder right",
    "UDAP",
    "UDTP",
    "water resource",
    "worker protection",
])

keyword_to_include = set([
    "environmental",
    "biodiversity",
    # "climate change",
    "climate goal",
    "emission",
    "sustainable",
    # "greenhouse gas",
    "water resource",
    "marine resource",
    # "natural resource",
    "pollution",
    "pollutant",
    # "pollute",
    "ecosystem",
    "carbon",
    # "DEI",
    # "diversity, equity and inclusion",
    "diversity",
    # "forced labor",
    # "human right",
    # "right to",
    "community impact",
    # "Equal pay",
    "discrimination",
    "harassment",
    "sexual harassment",
    "racial harassment",
    "wage",
    "labor condition",
    "child labor",
    # "working condition",
    # "employee relation",
    "algorithm",
    "machine learning",
    # "fraud",
    # "privacy",
    "data breach",
    "monopolies"
])


# Process the data
processed_data = {}
for industry, industry_data in data.items():
    num_words_in_industry = industry_data.pop("NUM WORDS IN INDUSTRY", None)
    if num_words_in_industry is None:
        continue

    processed_keywords = {}
    for topic, keywords in industry_data.items():
        for keyword, count in keywords.items():
            # Do not add these keywords
            if keyword in keywords_to_remove:
                continue

            # Only add these keywords
            if keyword not in keyword_to_include:
                continue

            # Normalize the word count and store it in the processed_keywords dictionary
            normalized_count = count / num_words_in_industry

            # Write normalized count as a percentage
            normalized_count = normalized_count * 100

            processed_keywords[keyword] = normalized_count

    processed_data[industry] = processed_keywords

# Save the processed data to a new JSON file
# with open("./wordcounts/environmental.json", "w") as output_file:
with open("./processed_word_count.json", "w") as output_file:
    json.dump(processed_data, output_file, indent=4)
