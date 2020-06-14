# Simple calculator (Made: Jauaries).

import math

def add(x, y):
    a = x + y
    return a

def subtract(x, y):
    s = x - y
    return s

def multiply(x, y):
    m = x * y
    return m

def divide(x, y):
    d = x / y
    return d

def power(x,y):
    p = pow(x,y)
    return p


print("Select the operation that you want:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Power")

choice = input("Enter your choice(| 1 | 2 | 3 | 4 | 5 |): ")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if choice == '1':
    print("%s + %s = %s" %(num1, num2, add(num1, num2)))
elif choice == '2':
    print("%s - %s = %s" %(num1, num2, subtract(num1, num2)))
elif choice == '3':
    print("%s * %s = %s" %(num1, num2, multiply(num1, num2)))
elif choice == '4':
    print("%s / %s = %s" %(num1, num2, divide(num1, num2)))
elif choice == '5':
    print("%s ^ %s = %s" %(num1, num2, power(num1, num2)))
else:
    print("Invalid input.")
