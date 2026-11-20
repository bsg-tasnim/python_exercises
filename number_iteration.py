# Iterate through 10 numbers. 
# In each iteration, print the current number, the previous number, and their sum.

numbers=range(10,20)

for n in numbers:
    prev=n-1
    sum=prev+n
    print(f"current number: {n}, previous number: {prev}, sum: {sum}")
    n=n+1
   
    

