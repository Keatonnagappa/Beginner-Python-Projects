# Password Generator Project
import random
# Setting up lists for possible combinations
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Prompting for input
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Initialize the password variables to ""
# Use for loops to pull random letters,symbols and numbers from various lists
# The amount of times these loops run are based on user input
password = []
for char in range(1, nr_letters + 1):
    password.append(random.choice(letters))

for symbol in range(1, nr_symbols + 1):
    password.append(random.choice(symbols))

for number in range(1, nr_numbers + 1):
    password.append(random.choice(numbers))

# Randomizing the order of characters
random.shuffle(password)

# Converting list output into a string to make it more readable
password_string = ""
for char in password:
    password_string += char

# Outputting result
print(f"Your password is: {password_string}")

# Alternatively if we went with assigning values to a string instead of appending to a list we could do the following to shuffle the result

#p = list(password)
# random.shuffle(p)
#result= "".join(p)
#print(f"Your password is: {result}")
