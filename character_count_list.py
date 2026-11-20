#Create a list of 5 words. Write a loop that iterates through the list and 
#prints each word alongside its character count.

list=["a","ab","abc","abcd","abcde"]
for i in list :
    x=len(i)
    print(f"{i}={x}")