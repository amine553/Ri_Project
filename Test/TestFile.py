import os

folder_path = r'C:\Users\hacia\Desktop\Ri_Project\Collection_TIME'

collection = []
# Loop through all files in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
    # Check if the file is a regular file (not a directory)
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            # Read the content of the file and add it to the collection list
            collection.append(file.read().strip())

for text in collection :
    
    print(text)
    print("----------------------------------------------------------------------------------\n\n\n\n")
    