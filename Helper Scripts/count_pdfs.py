import os

def count_pdfs(directory):
    pdf_count = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_name, file_ext = os.path.splitext(file)
            if file_ext.lower() == '.pdf':
                pdf_count += 1

    return pdf_count


root_dir = 'downloads'  # Replace 'your_directory' with the path of the directory you want to scan
pdf_count = count_pdfs(root_dir)
print(f'There are {pdf_count} PDF files in the directory "{root_dir}".')
