import os

# Path to the directory containing the images
directory = 'C:\Desktop\maj\RealArt'

# Loop through all files in the directory
for count, filename in enumerate(os.listdir(directory)):
    # Construct the new filename
    new_name = f"{count + 1}.jpg"
    # Get the full path to the current file
    src = os.path.join(directory, filename)
    # Get the full path to the new file
    dst = os.path.join(directory, new_name)
    # Rename the file
    os.rename(src, dst)

print("Renaming completed!")
