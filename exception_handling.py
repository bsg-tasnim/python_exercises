#Write a function read_file(filename) that opens a file manually (without a with statement), 
# reads its contents, and uses a finally block to ensure the file handle is always closed, 
# whether the read succeeds or an exception is raised.

def read_file(file):
    f=None
    try:
        f=open(file,"r")
        content=f.read()
        print(content)
    except FileNotFoundError:
        print(f"Error: File was not found. Please check the file name and try again.")
    finally:
        if f:
            f.close()
        print(f"File {file} has been closed.")

read_file("/home/blockstak/Documents/program/test_data.csv")
read_file("invalid.txt")