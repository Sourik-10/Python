import os

# List all files and folders inside the 'dir' directory
f = os.listdir("dir")
print(f)

# Print the current working directory
print(os.getcwd())

# Check whether a file or folder named 'file' exists in the current directory
print(os.path.exists("file"))

# Remove the file 'sample.txt' from inside the 'dir' directory
os.remove("dir/sample.txt")

# Remove the directory 'dir'
# Note: The directory must be empty for os.rmdir() to work
os.rmdir("dir")
