import os
import sys

"""
Deletes all instances of a specific file name.
Helpful for cleaning up directories.
"""

if len(sys.argv) < 2:
    print("Usage: python delete.py file_to_delete")
    sys.exit(1)

directory_path = "downloads"
file_to_delete = sys.argv[1]

for root, dirs, files in os.walk(directory_path):
    for file in files:
        if file == file_to_delete:
            file_path = os.path.join(root, file)
            try:
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            except OSError as e:
                print(f"Error deleting {file_path}: {e}")
