import csv

input_file = "downloads/all_context.txt"
output_file = "downloads/all_context.csv"

industry = None
case_number = None
topic = None
keyword = None

with open(input_file, "r") as infile, open(output_file, "w", newline='') as outfile:
    csv_writer = csv.writer(outfile)
    csv_writer.writerow(["Industry", "Case Number", "Topic", "Keyword", "Example"])

    for line in infile:
        stripped_line = line.strip()

        if stripped_line.startswith("=== INDUSTRY:"):
            industry = stripped_line[len("=== INDUSTRY:"):].strip().rstrip("===").strip()
        elif stripped_line.startswith("---"):
            case_number = stripped_line[len("---"):].strip().rstrip("---").strip()
        elif ": " in stripped_line:
            topic, keyword = stripped_line.split(": ", 1)
        elif stripped_line != "":
            example = stripped_line
            csv_writer.writerow([industry, case_number, topic, keyword, example])
