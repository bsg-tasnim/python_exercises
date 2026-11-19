#Write a function to remove characters from a string starting from index 0 up to n and return a new string.

string=input("Enter a string: ")

x=int(input("Enter number of characters to remove: "))

result=string[x::1]
print(result)
