#Write a Python function that accepts two integer numbers. 
# If the product of the two numbers is less than or equal to 1000, return their product; 
# otherwise, return their sum.

def conditional_sum(num1,num2):
    prod=num1*num2
    sum=num1+num2
    if prod<=1000:
        return prod
    else:
        return sum

num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd number: "))

result=conditional_sum(num1,num2)

print(f"Result is {result}")