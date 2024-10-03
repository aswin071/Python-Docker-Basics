# Python Essential Training Notes

# 1. Basic Syntax
# - Python uses indentation (spaces or tabs) to define code blocks.
# - Comments start with a '#' symbol and are ignored by the interpreter.

# 2. Data Types
# - int: Integer values (e.g., 42)
# - float: Floating-point values (e.g., 3.14)
# - str: String values (e.g., "Hello, World!")
# - bool: Boolean values (True or False)
# - list: Ordered, mutable collection (e.g., [1, 2, 3])
# - tuple: Ordered, immutable collection (e.g., (1, 2, 3))
# - dict: Unordered, mutable collection of key-value pairs (e.g., {"key": "value"})

# 3. Variables
# - Use meaningful variable names and follow naming conventions (snake_case).
# - Variable assignment: x = 10

# 4. Control Flow
# - Conditional statements: if, elif, else
# Example:
# if x > 0:
#     print("Positive")
# elif x < 0:
#     print("Negative")
# else:
#     print("Zero")

# 5. Loops
# - for loop: Iterates over a sequence (list, tuple, string, etc.)
# Example:
# for i in range(5):
#     print(i)

# - while loop: Executes as long as a condition is true.
# Example:
# while x > 0:
#     print(x)
#     x -= 1

# 6. Functions
# - Define functions using the def keyword.
# - Example:
# def greet(name):
#     return f"Hello, {name}!"

# - Function arguments can have default values.
# Example:
# def add(a, b=5):
#     return a + b

# 7. Error Handling
# - Use try and except blocks to handle exceptions.
# Example:
# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
# finally:
#     print("Execution completed.")

# 8. Object-Oriented Programming (OOP)
# - Define classes using the class keyword.
# - Use __init__() for constructors.
# Example:
# class Dog:
#     def __init__(self, name):
#         self.name = name
#     def bark(self):
#         return f"{self.name} says woof!"

# 9. Inheritance
# - Inherit from a base class.
# Example:
# class Puppy(Dog):
#     def play(self):
#         return f"{self.name} is playing!"

# 10. Threading
# - Use the threading module to run code in parallel.
# Example:
# import threading
#
# def print_numbers():
#     for i in range(5):
#         print(i)
#
# thread = threading.Thread(target=print_numbers)
# thread.start()
# thread.join()  # Wait for the thread to finish

# 11. Best Practices
# - Follow PEP 8 style guide for Python code.
# - Write docstrings for functions and classes.
# - Use version control (e.g., Git) for tracking changes.

# 12. Libraries and Frameworks
# - Explore popular libraries like NumPy, Pandas, Flask, and Django for extended functionality.
