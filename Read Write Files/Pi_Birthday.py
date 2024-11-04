# Open the file in read mode
pi = open("Read Write Files/pi_million_digits.txt")

# Open the file in read mode
pi = open("Read Write Files/pi_million_digits.txt")  

# Print the first line and close the file
print(pi.readline())  
pi.close() 

# Reopen the file and read all lines into a list
pi = open("Read Write Files/pi_million_digits.txt")  
pi_lines = pi.readlines()
pi.close()

# Get user's birthday
user_birthday = input("Enter your birthday in the format MMDDYY: ")

# Initialize a variable to track if the birthday is found
birthday_found = None  

# Loop through the lines of the file
for i in pi_lines:
    if user_birthday in i:
        print("Your birthday is in the first million digits of pi")
        birthday_found = 1  # Update the tracker if the birthday is found
        break

# Print a message if the birthday is not found
if birthday_found != 1:  
    print("Sorry, your birthday was not found in the first million digits of pi")

# Print the first two lines and their lengths for analysis
# print(pi_lines[0])
# print(len(pi_lines[0]))
# print(pi_lines[1])
# print(len(pi_lines[1]))

# Concatenate the lines into a single string
pi_string = ''
for i in pi_lines:
    pi_string += i.strip()  # Remove extra spaces and newline characters

# Find the position of the birthday if it was found
if birthday_found == 1:
    birthday_position = pi_string.index(user_birthday) - 1  
    # -1 because indexing starts at 0 and pi starts with '3.'
    print(f"Your birthday begins at decimal place {birthday_position}")
