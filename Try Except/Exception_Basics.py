# ValueError example
try:
    num = int("abc")  # Trying to convert a non-numeric string to an integer
except ValueError:
    print("Oops! That was not a valid number. Please try again.")
else:
    print(f"The number is: {num}")
finally:
    print("Let's try another one.")

# NameError example
try:
    print(unknown_variable)  # Trying to access a variable that doesn't exist
except NameError:
    print("Oops! That variable doesn't exist. Please check your code.")
else:
    print("No errors found.")
finally:
    print("Let's try another one.")

# TypeError example
try:
    result = "hello" + 123  # Trying to concatenate a string and an integer
except TypeError:
    print("Oops! You can't perform that operation on those data types.")
else:
    print(f"The result is: {result}")
finally:
    print("Let's try another one.")

# SyntaxError example
try:
    exec("print('Hello, world!'")  # Missing a closing parenthesis
except SyntaxError:
    print("Oops! There's a syntax error in your code. Please check it and try again.")
else:
    print("No errors found.")
finally:
    print("Let's try another one.")