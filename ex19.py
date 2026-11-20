#Write a program that tries to open a file that does not exist on disk. 
# Catch the FileNotFoundError exception and display a clear, user-friendly message 
# instead of showing a raw Python traceback.

file="invalid.txt"

try:
    with open(file,'r') as f:
        content=f.read()
        print(content)

except FileNotFoundError:
    print(f"Error: File was not found. Please check the file name and try again.")
