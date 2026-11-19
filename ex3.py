#Display only those characters which are present at an even index number in given string.

string=input("Enter a string: ")

print("Method 1")
for i in range(len(string)):
   
   if i%2==0:
      print(string[i])


print(f"Method 2:",string[::2])
