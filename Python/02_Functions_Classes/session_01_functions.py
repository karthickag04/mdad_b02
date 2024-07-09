#!/usr/bin/env python
# coding: utf-8

# This section demonstrates arithmetic and comparison operators
x = 10
y = 20

# Arithmetic operators
print(x + y)  # Addition
print(x * y)  # Multiplication
print(x - y)  # Subtraction
print(x / y)  # Division
print(x % y)  # Modulus
print(x ** y) # Exponentiation

# Comparison operators
print(x == y)  # Equal to
print(x < y)   # Less than
print(x > y)   # Greater than
print(x <= y)  # Less than or equal to
print(x >= y)  # Greater than or equal to

# Function demonstrating arithmetic operations
def operatordemo():
    z = 10
    v = 10
    print(z + v)  # Addition
    print(z - v)  # Subtraction
    print(z * v)  # Multiplication
    print(z / v)  # Division

# Calling the function multiple times
operatordemo()
operatordemo()
operatordemo()
operatordemo()

# Function demonstrating addition with formatted print statements
def addition():
    z = 10
    v = 11
    print("added value of z and v is", z + v)
    print("added value of z:", z, "and v:", v, "is", z + v)
    print(f"added value of z: {z} and v: {v} is", z + v)

addition()

# Function demonstrating addition with a return statement
def additionr():
    z = 10
    v = 11
    return z + v

# Calling the function with return value
result_1 = addition()
result_2 = additionr()

# Printing the results
print(result_1)
print(result_2)

# Conditional check on the return values
if result_1 == 21:
    print("it's equal under normal")
if result_2 == 21:
    print("it's equal under return")

# Function demonstrating addition with arguments
def addition_with_args(z, v):
    return z + v

# Calling the function with arguments
addition_with_args(10, 31)

# Function demonstrating multiple arithmetic operations with comments
def operatordemo1(x, y):
    """This function takes two numbers and performs various operations"""
    print("addition", x + y)
    print("addition", x + y)
    print("addition", x + y)
    print("addition", x + y)
    print("addition", x + y)
    print("addition", x + y)
    print("addition", x + y)

# Function demonstrating operations based on an operator symbol
def operator_with_if(operator_symbol, x, y):
    if operator_symbol == '+':
        print("addition", x + y)
    elif operator_symbol == '-':
        print("subtraction", x - y)
    elif operator_symbol == '*':
        print("multiplication", x * y)
    else:
        print("division", x / y)

# Calling the function with operator symbol and arguments
operator_with_if('+', 33, 22)
