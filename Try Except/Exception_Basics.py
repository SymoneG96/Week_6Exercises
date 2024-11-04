# ValueError
while True:
    try:
        user_input = input("Enter a number: ")
        number = int(user_input)  # Trying to convert user input to an integer
        break  # Exit the loop if no error occurs
    except ValueError:
        print("Hmm, that doesn't look like a number. Try entering a whole number, like 1, 5, or 100.")
print(f"You entered: {number}")
print("Let's try another one...\n")

# NameError
while True:
    try:
        user_input = input("Enter a variable name: ")
        print(eval(user_input))  # Trying to print the value of the variable entered by the user
        break  # Exit the loop if no error occurs
    except NameError:
        print("Oops! It seems like that variable hasn't been defined yet. Make sure you've created it before trying to use it.")
print("Variable found!")
print("Let's try another one...\n")

# TypeError
while True:
    try:
        user_input1 = input("Enter a string: ")
        user_input2 = int(input("Enter a number: "))
        result = user_input1 + user_input2  # Trying to add a string and an integer
        break  # Exit the loop if no error occurs
    except TypeError:
        print("Whoops! You can't add a word and a number directly. Try converting them to the same type first.")
print(f"Result: {result}")
print("Let's try another one...\n")

# SyntaxError
while True:
    try:
        user_input = input("Enter a Python expression: ")
        eval(user_input)  # Trying to evaluate the expression entered by the user
        break  # Exit the loop if no error occurs
    except SyntaxError:
        print("Uh oh, looks like there's a syntax error in your expression. Double-check for any typos or missing symbols.")
print("Expression evaluated successfully!")
print("Let's try another one...\n")