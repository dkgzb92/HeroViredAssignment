import os
import shutil
import sys
from datetime import datetime

def backup_files(source_dir, dest_dir):
    # Check if the source directory exists
    if not os.path.exists(source_dir):
        print(f"Source directory '{source_dir}' does not exist.")
        return

    # Create the destination directory if it doesn't exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Iterate over the files in the source directory
    for filename in os.listdir(source_dir):
        source_file = os.path.join(source_dir, filename)
        dest_file = os.path.join(dest_dir, filename)

        # Check if a file with the same name already exists in the destination directory
        while os.path.exists(dest_file):
            # Append a timestamp to the filename to ensure uniqueness
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            base, extension = os.path.splitext(filename)
            filename = f"{base}_{timestamp}{extension}"
            dest_file = os.path.join(dest_dir, filename)

        # Copy the file to the destination directory
        shutil.copy2(source_file, dest_file)
        print(f"Backed up: {source_file} to {dest_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python backup.py source_dir dest_dir")
    else:
        source_dir = sys.argv[1]
        dest_dir = sys.argv[2]
        backup_files(source_dir, dest_dir)
