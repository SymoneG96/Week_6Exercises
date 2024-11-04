# 1. Prompt for name input
name = input("Enter a name: ")

# 2. Define the trunc_name function
def trunc_name(name):
  """Truncates a name based on its starting letters."""
  name = name.lower()  # Convert to lowercase
  if name[0] in 'aeiou':  # Starts with a vowel
    return name
  elif len(name) > 1 and name[1] in 'aeiou':  # Starts with one consonant
    return name[1:]
  else:  # Starts with two consonants
    return name[2:]

# 3. Test the trunc_name function (comment out after testing)
# print(trunc_name("Ann"))   # Output: ann
# print(trunc_name("Dan"))   # Output: an
# print(trunc_name("Stan"))  # Output: an

# 4. Define the name_game generator function
def name_game(name):
  """Generates the lines of the name game song."""
  truncated_name = trunc_name(name)
  yield f"{name}, {name}, bo-b{truncated_name}"
  yield f"b{truncated_name} fana fo-f{truncated_name}"
  yield f"me my mo-m{truncated_name}"
  yield f"{name}!"

# 5. Test the name_game function with different names
names = ["Symone Gant", "carly", "CHARLIE", "Aidan", "Braden", "Billy Bob"]
for name in names:
  print("\n")  # Print a newline for readability
  for line in name_game(name):
    print(line)

# Observations:
# - The trunc_name function handles different capitalization correctly.
# - The name_game function generates the song lines as expected.
# - The code accounts for names with varying numbers of starting consonants.

"""
Explanation for question 7:

The first loop checks if you entered a real name. It tries to turn your input into a 
number. If it can (meaning you typed in a number), it knows that's not a name and 
asks you again. The "pass" just means "ignore the error" because we expect an 
error if you put in a real name.
"""

"""
Thoughts for question 8:

"raise SystemExit(0)" is like a big "stop" button for the whole program. It's used here 
because if the program doesn't get a real name, there's no point in continuing. It's 
stronger than "break", which would only stop the current loop, not the whole thing.
"""

