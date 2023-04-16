# FTC Lawsuit Data Analysis
## Summary
Technology is advancing at an unprecedented rate, but our legal system is struggling to keep up. That's why we conducted this data analysis on thousands of lawsuits issued by the Federal Trade Commission.

By examining the frequency of specific terms related to environmental, social, and governance issues, we identified critical gaps in the legal framework that leave companies unchecked and consumers vulnerable. Our findings provide a critical first step toward quantifying missing law. By shedding light on these issues, we hope to raise awareness of unaddressed problems in our legal system, promote better regulation of the tech industry, and inspire policy changes.

**Team members**: Benny Craig, Cecilia Brisuda, Oviyan Anbarasu, Yogi Sahu

**Social Consequences of Computing** at University of Michigan

## Code

This is the order in which these Python scripts were run:
1. `downloads.py` (downloads court case documents from FTC website)
2. `duplicates.py` (removes duplicate files)
3. `wordcount.py` (counts words and gets context of word match)
4. `industry.py` (aggregates all word counts and contexts)
5. `aggregate_all_industries.py` (aggregates all industries into final results)
6. `csv_conversion.py` (converts all JSON files to CSV)
7. `process_wordcount.py` (reads in word count and outputs the normalized word count)
8. `plot_heatmap.py` (creates the heat map of word counts across industries)

Here are some additional helper scripts
- `delete.py` (used to clean up unneeded files created)
- `count_folders.py` (counts the total number of cases)
- `count_pdfs.py`  (counts the total number of documents)
- `context_to_csv.py` (converts context.txt to CSV for spreadsheet viewing)



## Data Gathered
Here is a glimpse at the data we gathered:
- Downloaded over 4,500 PDFs from the FTC containing information on 1,020 lawsuits organized by industry
- Gathered word counts for over 100 search terms across 35 industries (searched over 29 million words in the process)
- Gathered surrounding words for each search match to easily see the context of the word usage and refer back to the original document in which the match was found


<img width="969" alt="Screenshot 2023-04-15 at 7 17 04 PM" src="https://user-images.githubusercontent.com/57501435/232257899-ccd25a79-7968-4d5f-b9a7-b6387e33e376.png">


## Graphical Results

<img width="928" alt="Screenshot 2023-04-15 at 7 02 09 PM" src="https://user-images.githubusercontent.com/57501435/232257820-42d00ab3-471c-426f-b718-901047a40a0d.png">

<img width="822" alt="Screenshot 2023-04-15 at 7 15 57 PM" src="https://user-images.githubusercontent.com/57501435/232257903-43b0a588-1f03-4694-b192-091474f599ee.png">

<img width="941" alt="Screenshot 2023-04-15 at 8 03 34 PM" src="https://user-images.githubusercontent.com/57501435/232259203-9ce0d3bc-69c3-4f46-9747-61da5e279969.png">

<img width="923" alt="Screenshot 2023-04-15 at 8 05 05 PM" src="https://user-images.githubusercontent.com/57501435/232259244-3bb9726c-dab6-447e-80bc-09f74cee1f64.png">

