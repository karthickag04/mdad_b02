# normal method to get input from user through terminal
def addition():
    # Taking two inputs from the user and converting them to integers
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    # Returning the sum of the two numbers
    return a + b

# Printing the result of the addition function
print("Added value of a and b:", addition())



# Class in Python
# A class starts with the 'class' keyword followed by the class name

# First version of the class with user input within methods
class ArithmeticOperations1:
    # Method for addition
    def addition(self):
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        return a + b
    
    # Method for subtraction
    def subtraction(self):
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        return a - b
    
    # Method for multiplication
    def multiplication(self):
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        return a * b

# Creating an instance of the class
ao1 = ArithmeticOperations1()

# Calling methods and printing their results
print(ao1.addition())
added_value = ao1.addition()
print("Added value of a and b:", added_value)
print("Added value of a and b direct call:", ao1.addition())
print("Subtracted value of a and b:", ao1.subtraction())
print("Multiplied value of a and b:", ao1.multiplication())


# Second version of the class with parameters in methods
class ArithmeticOperations2:
    # Method for addition
    def addition(self, a, b):
        return a + b
    
    # Method for subtraction
    def subtraction(self, a, b):
        return a - b
    
    # Method for multiplication
    def multiplication(self, a, b):
        return a * b

# Creating an instance of the class
ao2 = ArithmeticOperations2()

# Calling methods with arguments and printing their results
print("Added value of a and b through arguments to each method:", ao2.addition(10, 20))
print("Subtracted value of a and b through arguments to each method:", ao2.subtraction(10, 20))
print("Multiplied value of a and b through arguments to each method:", ao2.multiplication(10, 20))

# Taking input from the user and passing to methods
a = int(input("Enter value a: "))
b = int(input("Enter value b: "))
print("Added value of a and b through arguments to each method:", ao2.addition(a, b))
print("Subtracted value of a and b through arguments to each method:", ao2.subtraction(a, b))
print("Multiplied value of a and b through arguments to each method:", ao2.multiplication(a, b))


# Third version of the class with constructor and user input inside constructor
class ArithmeticOperations3:
    def __init__(self):
        # Taking input from the user when the object is created
        self.a = int(input("Enter value a: "))
        self.b = int(input("Enter value b: "))
        
        # Performing operations and printing results
        self.addition(10, 10)
        self.subtraction(10, 10)
        self.multiplication(self.a, self.b)
    
    def addition(self, a, b):
        print(f"Added value of a and b: {a + b}")
    
    def subtraction(self, a, b):
        print(f"Subtracted value of a and b: {a - b}")
    
    def multiplication(self, a, b):
        print(f"Multiplication of a and b: {a * b}")

# Creating an instance of the class which triggers the constructor
ao3 = ArithmeticOperations3()


# Fourth version of the class with constructor accepting parameters
class ArithmeticOperations4:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
        print("Welcome to constructor auto run")
        # Performing operations and printing results
        self.addition()
        self.subtraction()
        self.multiplication()
    
    def addition(self):
        print(f"Added value of a and b: {self.a + self.b}")
    
    def subtraction(self):
        print(f"Subtracted value of a and b: {self.a - self.b}")
    
    def multiplication(self):
        print(f"Multiplication of a and b: {self.a * self.b}")

# Creating an instance of the class with parameters, which triggers the constructor
ao4 = ArithmeticOperations4(int(input("Enter value a: ")), int(input("Enter value b: ")))
