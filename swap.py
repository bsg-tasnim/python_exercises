#Write a program to swap the values of two variables, a and b, without using a third temporary variable.

a=int(input("Enter a number: "))
b=int(input("Enter a number: "))


print(f"Before swapping: ", a,b)

a,b=b,a

print(f"After swapping: ", a,b)
