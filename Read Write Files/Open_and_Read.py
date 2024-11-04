# First version of the script
file = open('about_me.txt', 'r')
print(file.read())
file.close()

# My modified version with two read(50) calls
file = open('about_me.txt', 'r')
print("First read(50):")
print(file.read(50))
print("\nSecond read(50):")
print(file.read(50))
file.close()

"""
In my first version, I'm doing three simple things:
* I'm opening my file in read mode ('r')
* I'm reading and printing all the contents with `read()`
* I'm closing my file when I'm done

When I modified my script to use `read(50)`, here's what I discovered:
* My first `read(50)` reads the first 50 characters from my file
* My second `read(50)` reads the next 50 characters from where I left off
* This works because my file keeps track of where I stopped reading, like using a bookmark

When I run my modified version, I can see that:
1. My first `print(file.read(50))` shows me the first 50 characters of my file
2. My second `print(file.read(50))` shows me the next 50 characters
3. My file pointer moves forward each time I read

I found this interesting because it shows me how Python remembers my place in the file - just like when I'm
reading a book and use a bookmark to keep track of where I stopped. Each time I use `read(50)`, it's like
moving my bookmark forward by 50 characters.
"""

# New version experimenting with readline()
file = open('about_me.txt', 'r')

print("Reading first 10 characters of a line:")
print(file.readline(10))

print("\nReading an entire line:")
print(file.readline())

print("\nReading next 4 lines using a loop:")
for i in range(1, 5):
    print(f"Line {i}: {file.readline()}", end='')

file.close()

""" 
When I run my modified version, I can see that:
1. My first `print(file.read(50))` shows me the first 50 characters of my file
2. My second `print(file.read(50))` shows me the next 50 characters
3. My file pointer moves forward each time I read

Now I'm experimenting with readlines():
* readlines() returns a list of all lines in the file
* The size hint (like readlines(1) or readlines(10)) suggests approximately how many bytes to read
* The actual lines returned depend on line lengths since readlines() won't split lines
* readlines(-1) reads all lines, just like readlines() with no argument
* Once all lines are read, subsequent readlines() calls return an empty list
"""

# New version experimenting with readlines()
file = open('about_me.txt', 'r')

print("First readlines(1):")
print(file.readlines(1))

print("\nSecond readlines(1):")
print(file.readlines(1))

print("\nreadlines(10):")
print(file.readlines(10))

print("\nAnother readlines(10) with previous calls commented out:")
# Comment out the previous readlines() calls and uncomment this:
# print(file.readlines(10))

print("\nreadlines(100):")
print(file.readlines(100))

print("\nreadlines(-1):")
print(file.readlines(-1))

file.close()

"""
Now I'm combining different read methods:
* read(50) gets exactly 50 characters
* readline() in a loop builds a list line by line
* readlines(100) gets complete lines up to about 100 bytes
* Each read method continues from where the previous left off
"""

file = open('about_me.txt', 'r')

# Get first 50 characters
first_fifty = file.read(50)

# Get next four lines as a list
next_four_lines = []
for i in range(4):
    next_four_lines.append(file.readline())

# Get next ~100 bytes as complete lines
next_hundred = file.readlines(100)

# Print results with descriptive labels
print("First 50 characters:")
print(first_fifty)

print("\nNext four lines, as list by line:")
print(next_four_lines)

print("\nNext 100 characters, as list by line, rounded up to complete lines:")
print(next_hundred)

file.close()