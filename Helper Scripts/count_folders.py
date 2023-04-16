import os

# Specify the directory path to count folders in
path = "downloads"

# Initialize a count variable
count = 0

# Walk through the directory tree and count subdirectories
for dirpath, dirnames, filenames in os.walk(path):
    count += len(dirnames)

# Print the number of folders
print("The directory", path, "contains", count, "folders.")