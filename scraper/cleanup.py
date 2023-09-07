import os
import hashlib

def calculate_sha256(file_path):
    hash_sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha256.update(chunk)
    return hash_sha256.hexdigest()

def count_words(file_path):
    with open(file_path, 'r') as f:
        text = f.read()
    return len(text.split())

def delete_duplicate_and_empty_files(directory):
    file_hashes = {}
    files_to_delete = []

    # Step 1: List all files
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        if os.path.isfile(file_path):
            try:
                # Identify empty or near-empty text files
                if count_words(file_path) < 10:
                    print(f"Deleting empty or near-empty file: {file_path}")
                    os.remove(file_path)
                    continue
            except UnicodeDecodeError:
                # Skip files that are not text files
                pass

            # Compute hash for remaining files
            file_hash = calculate_sha256(file_path)

            # Identify duplicates
            if file_hash in file_hashes:
                files_to_delete.append(file_path)
            else:
                file_hashes[file_hash] = file_path
                
    # Remove duplicates
    for file_path in files_to_delete:
        print(f"Deleting duplicate file: {file_path}")
        os.remove(file_path)

# Get the parent directory of the current script
parent_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define the 'text' directory under the same parent directory
text_directory = os.path.join(parent_directory, 'text')

# Run the function
delete_duplicate_and_empty_files(text_directory)
