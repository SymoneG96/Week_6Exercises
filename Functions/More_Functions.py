def display_mailing_label(name, address1, address2, city, state, zip):
  """Displays a mailing label with the given information."""
  print(name)
  print(address1)
  if address2:  # Print address2 only if it's provided
    print(address2)
  print(f"{city}, {state} {zip}")
  print()  # Add an empty line


def add_numbers(*numbers):
  """Adds the given numbers and displays the result."""
  result = sum(numbers)
  print(" + ".join(str(num) for num in numbers), "=", result)
  print()  # Add an empty line


def display_receipt(total_due, amount_paid):
  """Displays a receipt with total due, amount paid, and change due."""
  print("Total Due: $", total_due)
  print("Amount Paid: $", amount_paid)
  if amount_paid >= total_due:
    print("Change Due: $", amount_paid - total_due)
  else:
    print("Balance Due: $", total_due - amount_paid)
  print()  # Add an empty line


# Call the functions with Chicago and New York addresses
display_mailing_label("Michael Jordan", "2300 S Indiana Ave", "", "Chicago", "IL", "60616")
display_mailing_label("Lady Liberty", "Liberty Island", "", "New York", "NY", "10004")

add_numbers(10)
add_numbers(5, 7)
add_numbers(2, 4, 6, 8)

display_receipt(15.75, 20)  # Overpay
display_receipt(10, 10)  # Pay exactly
display_receipt(12.50, 10)  # Underpay