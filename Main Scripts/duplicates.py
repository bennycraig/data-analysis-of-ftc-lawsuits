import os
import hashlib

"""
This script checks for duplicate files in the downloads folder.

NOTE: os.remove() is commented out so that this will only display the duplicates
        Uncomment those two lines to remove all the duplicates

ANOTHER NOTE: You can either find duplicates WITHIN one case folder, or find duplicates
across ALL cases and industries. This depends on whether you initialize the file_hashes
dictionary inside or outside the for loop.
"""


# Define a function to get the MD5 hash of a file
def get_file_hash(filename):
    with open(filename, "rb") as f:
        file_contents = f.read()
        return hashlib.md5(file_contents).hexdigest()

# Define the root directory to search
root_dir = "downloads 2"

# Keep track of duplicates
total_duplicates = 0


# If you construct dictionary here, you will find duplicates across ALL cases
# file_hashes = {}

# Walk through the directory tree and find all files
for dirpath, dirnames, filenames in os.walk(root_dir):
    
    # Create a dictionary to store hashes & corresponding file
    file_hashes = {}

    for filename in filenames:
        # Get the full path of the file
        file_path = os.path.join(dirpath, filename)
        # Get the MD5 hash of the file
        file_hash = get_file_hash(file_path)
        # Check if the file hash has already been seen
        if file_hash in file_hashes:
            # Increment duplicates
            total_duplicates += 1
            # Get the existing file path with the same hash
            existing_file_path = file_hashes[file_hash]
            # If the new filename is longer, remove it
            if len(filename) > len(os.path.basename(existing_file_path)):
                # os.remove(file_path)
                print(f"Keeping : {existing_file_path}")
                print(f"Removing: {file_path}")
            # Otherwise, remove the last seen one and store the new one
            else:
                # os.remove(existing_file_path)
                print(f"Keeping : {file_path}")
                print(f"Removing: {existing_file_path}")
                file_hashes[file_hash] = file_path
            
            
        else:
            # If the file hash is new, add it to the dictionary
            file_hashes[file_hash] = file_path

print("Total duplicates found: ", total_duplicates)