
def conv_f_to_c(temp_f):
  """Converts temperature from Fahrenheit to Celsius."""
  temp_c = (temp_f - 32) * 5/9
  return round(temp_c)

# Fahrenheit temperatures to convert
temps_f = [212, 90, 72, 32, 0, -40]

# Convert and display the temperatures
for temp_f in temps_f:
  temp_c = conv_f_to_c(temp_f)
  print(f"{temp_f} degrees Fahrenheit is equal to {temp_c} degrees Celsius")