name = 'John Doe'

# Find the index of the space
space_index = name.find(' ')

# Extract the first name
first_name = name[:space_index]

# Extract the last name
last_name = name[space_index + 1:]

# Display the results
print("Full Name:", name)
print("First Name:", first_name)
print("Last Name:", last_name) 

def parse_and_display(name):
  """
  Parses a full name into first, middle (if any), and last names, and displays the results.

  Args:
    name: The full name as a string.
  """

  parts = name.split()
  num_parts = len(parts)

  if num_parts == 1:
    first_name = parts[0]
    middle_name = ""
    last_name = ""
  elif num_parts == 2:
    first_name = parts[0]
    middle_name = ""
    last_name = parts[1]
  elif num_parts == 3:
    first_name = parts[0]
    middle_name = parts[1]
    last_name = parts[2]
  else:
    print("Error: Name has too many parts.")
    return

  print("Full Name:", name)
  print("First Name:", first_name)
  if middle_name:
    print("Middle Name:", middle_name)
  print("Last Name:", last_name)
 


# Tests
parse_and_display('John Doe')
parse_and_display('Grace Flores')
parse_and_display('JB Oinonen')