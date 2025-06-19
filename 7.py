import os

# Get the current working directory
current_directory ='/' #os.getcwd()
print("Current Directory:", current_directory)

# List all files and directories in the current directory
print("\nContents of the Directory:")
for item in os.listdir(current_directory):
    print(item)
