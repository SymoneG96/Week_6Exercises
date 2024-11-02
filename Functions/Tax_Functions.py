
def get_soc_sec_tax(gross_pay):
  """Calculates the Social Security tax."""
  return round(gross_pay * 0.062, 2)

def get_medicare_tax(gross_pay):
  """Calculates the Medicare tax."""
  return round(gross_pay * 0.0145, 2)

def get_federal_tax(gross_pay, withholding_code):
  """Calculates the federal tax withholding."""
  if withholding_code == 0:
    tax_rate = 0.23
  elif withholding_code == 1:
    tax_rate = 0.21
  elif withholding_code == 2:
    tax_rate = 0.195
  elif withholding_code == 3:
    tax_rate = 0.185
  else:  # withholding_code 4+
    tax_rate = 0.18 - ((withholding_code - 4) * 0.005)
  return round(gross_pay * tax_rate, 2)

# Example
people = [
  {"gross_pay": 750, "withholding_code": 0},
  {"gross_pay": 1550, "withholding_code": 2},
  {"gross_pay": 1100, "withholding_code": 5}
]

for person in people:
  gross_pay = person["gross_pay"]
  withholding_code = person["withholding_code"]
  soc_sec_tax = get_soc_sec_tax(gross_pay)
  medicare_tax = get_medicare_tax(gross_pay)
  federal_tax = get_federal_tax(gross_pay, withholding_code)

  print(f"Gross pay: ${gross_pay}")
  print(f"Withholding code: {withholding_code}")
  print(f"Social Security tax: ${soc_sec_tax}")
  print(f"Medicare tax: ${medicare_tax}")
  print(f"Federal tax: ${federal_tax}")
  print()