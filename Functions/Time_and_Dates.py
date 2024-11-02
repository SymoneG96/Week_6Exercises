import datetime

# Get the current date and time
today = datetime.datetime.now()

# Print today's date in the specified format
print("Today is", today.strftime("%A, %B %d, %Y"))

# Define your birthday
birthday = datetime.date(1996, 7, 26)

# Print your birthday in the specified format
print("My birthday is", birthday.strftime("%m/%d/%Y"))

# Calculate the date 90 days from today
ninety_d = today + datetime.timedelta(days=90)

# Print the date 90 days from today in the specified format
print("90 days from today is", ninety_d.strftime("%B %d, %Y"))

# Define a dinner time
dinner_time = datetime.time(18, 30)  # 6:30 PM

# Print the dinner time in the specified format
print("Let's meet for dinner at", dinner_time.strftime("%I:%M %p")) 