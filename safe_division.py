# Create a function safe_divide(a, b) that divides a by b. 
# If b is zero, handle the ZeroDivisionError and return None instead of letting the program crash.

def safe_divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

x=safe_divide(10, 2)
y=safe_divide(10, 0)
print(x)
print(y)
