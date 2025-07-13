# Writing to a file
with open("sample.txt", "w") as file:
    file.write("Python File Handling\n")
    file.write("This is a new file.")

# Reading the file
with open("sample.txt", "r") as file:
    print(file.read())
