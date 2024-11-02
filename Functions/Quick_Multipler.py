# 1. Create the doubler lambda function
doubler = lambda n: n * 2

# 2. Test it out
print(doubler(8))    # Output: 16
print(doubler(-4))   # Output: -8
print(doubler('banana'))  # Output: bananabanana

# 3. Create the tripler lambda function
tripler = lambda n: n * 3

# 4. Test it out
print(tripler(8))    # Output: 24
print(tripler(-4))   # Output: -12
print(tripler('banana'))  # Output: bananabananabanana

# 5. Create the multiplier function
def multiplier(factor):
  return lambda n: n * factor

# Create multiplier variables for 4 through 10
quadrupler = multiplier(4)
quintupler = multiplier(5)
sextupler = multiplier(6)
septupler = multiplier(7)
octupler = multiplier(8)
nonupler = multiplier(9)
decupler = multiplier(10)

# 6. Test the new variables
print(quadrupler(5))    # Output: 20
print(quintupler(5))   # Output: 25
print(sextupler(5))    # Output: 30
print(septupler(5))   # Output: 35
print(octupler(5))    # Output: 40
print(nonupler(5))   # Output: 45
print(decupler(5))    # Output: 50