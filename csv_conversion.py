import json
import csv
import os

def json_to_csv(json_file, all_industries=False):
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Formatting for all_industries file (includes industry column)
    if all_industries:
        csv_data = [['Industry', 'Category', 'Keyword', 'Count']]
        for industry, industry_data in data.items():
            for category, keywords in industry_data.items():
                if category == "NUM WORDS IN INDUSTRY":
                    csv_data.append([industry, category, "", keywords])
                else:
                    for keyword, count in keywords.items():
                        csv_data.append([industry, category, keyword, count])
    # Formatting for the rest of files
    else:
        csv_data = [['Category', 'Keyword', 'Count']]
        for category, keywords in data.items():
            if category in ["NUM WORDS IN INDUSTRY", "NUM WORDS IN CASE", "NUM WORDS"]:
                csv_data.append([category, "", keywords])
            else:
                for keyword, count in keywords.items():
                    csv_data.append([category, keyword, count])

    csv_file = os.path.splitext(json_file)[0] + '.csv'

    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(csv_data)

    print(f"CSV file '{csv_file}' created.")


root_dir = 'downloads'

# Convert total_word_count JSON to CSV
total_json_file = os.path.join(root_dir, 'total_word_count.json')
if os.path.isfile(total_json_file):
    json_to_csv(total_json_file)

# Convert all_industries_word_count JSON to CSV
all_industries_json_file = os.path.join(root_dir, 'all_industries_word_count.json')
if os.path.isfile(all_industries_json_file):
    json_to_csv(all_industries_json_file, all_industries=True)

for industry in os.listdir(root_dir):
    industry_dir = os.path.join(root_dir, industry)
    if not os.path.isdir(industry_dir):
        continue

    # Convert industry_word_count JSON to CSV
    industry_json_file = os.path.join(industry_dir, 'industry_word_count.json')
    if os.path.isfile(industry_json_file):
        json_to_csv(industry_json_file)

    for case in os.listdir(industry_dir):
        case_dir = os.path.join(industry_dir, case)
        if not os.path.isdir(case_dir):
            continue

        # Convert word_count JSON to CSV
        case_json_file = os.path.join(case_dir, 'word_count.json')
        if os.path.isfile(case_json_file):
            json_to_csv(case_json_file)
