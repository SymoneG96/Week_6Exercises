def parse_part_code(part_code):
  """
  Parses a part code and returns the supplier code, product number, and size.

  Args:
    part_code: The part code in the format 'supplier:productcode-size'.

  Returns:
    A tuple containing the supplier code, product number, and size.
  """
  supplier_code, rest = part_code.split(':')
  product_num, size = rest.split('-')
  return supplier_code, product_num, size


# Example part codes
part_code1 = 'ABC:1234-S'
part_code2 = 'DEF:5678-L'
part_code3 = 'GHI:9012-XL'

# Process and display results for each part code
part_codes = [part_code1, part_code2, part_code3]

for part_code in part_codes:
  supplier_code, product_num, size = parse_part_code(part_code)
  print("Part Code:", part_code)
  print("Supplier Code:", supplier_code)
  print("Product Number:", product_num)
  print("Size:", size)
  