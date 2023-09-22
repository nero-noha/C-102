import os

# Define the source and destination directories
import shutil

# Define the source and destination file paths
source_file = 'C:\\Users\\dharp\\Desktop\\python\\Project 102\\main.py'
destination_dir = 'C:\Users\dharp\Desktop\python\Project 102'

# Use shutil.copy() to copy the file to the destination directory
shutil.copy(source_file, destination_dir)

print("File copied successfully!")

# List all files in the source directory
files = os.listdir(source_dir)

# Loop through each file and copy it to the destination directory
for file in files:
    source_path = os.path.join(source_dir, file)
    destination_path = os.path.join(destination_dir, file)

    # Check if the item is a file (not a directory) before copying
    if os.path.isfile(source_path):
        shutil.copy(source_path, destination_path)

print("Files copied successfully!")
