def conv_c_to_f(temp_c):
  """Converts temperature from Celsius to Fahrenheit."""
  temp_f = (temp_c * 9/5) + 32
  return round(temp_f)

# Celsius temperatures to convert
temps_c = [100, 45, 19, 0, -7, -40]

# Convert and display the temperatures
for temp_c in temps_c:
  temp_f = conv_c_to_f(temp_c)
  print(f"{temp_c} degrees Celsius is equal to {temp_f} degrees Fahrenheit") 