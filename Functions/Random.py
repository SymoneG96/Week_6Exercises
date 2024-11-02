import random

# randint() - returns a random integer from a given range
random_integer = random.randint(1, 10)  # Generate a random integer between 1 and 10
print("Random integer:", random_integer)
print("Random integer:", random.randint(1, 10))
print("Random integer:", random.randint(1, 10))

# random() - returns a random float number between 0 and 1
random_float = random.random()
print("\nRandom float:", random_float)
print("Random float:", random.random())
print("Random float:", random.random())

# choice() - returns a random element from a given sequence
my_list = ["apple", "banana", "cherry", "peach", "plum", "watermelon"]
random_element = random.choice(my_list)
print("\nRandom element:", random_element)
print("Random element:", random.choice(my_list))
print("Random element:", random.choice(my_list))

# choices() - returns a list with a random selection from a given sequence
random_elements = random.choices(my_list, k=3)  # Select 3 random elements
print("\nRandom elements:", random_elements)
print("Random elements:", random.choices(my_list, k=2))
print("Random elements:", random.choices(my_list, k=4))

# sample() - returns a sample of a given sequence
random_sample = random.sample(my_list, k=3)  # Sample 3 elements without replacement
print("\nRandom sample:", random_sample)
print("Random sample:", random.sample(my_list, k=2))
print("Random sample:", random.sample(my_list, k=4))

# shuffle() - takes a sequence and returns it in a random order
random.shuffle(my_list)  # Shuffle the list in place
print("\nShuffled list:", my_list)
random.shuffle(my_list)
print("Shuffled list:", my_list)