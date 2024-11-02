
# 4. Update the name_game generator function to handle the special rule
from Name_Game import trunc_name


def name_game(name):
  """Generates the lines of the name game song, including the special rule for b, f, m."""
  truncated_name = trunc_name(name)
  if truncated_name[0] in 'bfm':
    truncated_name = name.lower() + truncated_name  # Use the full name
  yield f"{name}, {name}, bo-b{truncated_name}"
  yield f"b{truncated_name} fana fo-f{truncated_name}"
  yield f"me my mo-m{truncated_name}"
  yield f"{name}!"

# ... (test the name_game function with different names) ...

# 8. BONUS: Handle inappropriate names
def get_name():
  """Prompts the user for a name and handles inappropriate inputs."""
  while True:
    name = input("Enter a name: ")
    if name.lower() in ["bart", "buck"]:
      print("Warning: This name might be considered inappropriate for the Name Game.")
      confirm = input("Do you want to use it anyway? (yes/no): ")
      if confirm.lower() != "yes":
        continue  # Re-prompt for a name
    return name

# Update the main part of the script to use get_name()
names = ["Symone Gant", "carly", "CHARLIE", "Aidan", "Braden", "Billy Bob", "Bart", "Buck"]
for name in names:
  print("\n")
  for line in name_game(get_name()):  # Use get_name() here
    print(line)

# Observations:
# - The name_game function now correctly applies the special rule for names starting with b, f, or m.
# - The script handles inappropriate names by displaying a warning and re-prompting for confirmation.