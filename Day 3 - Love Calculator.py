# Prompt for input
print("Welcome to the love calculator!")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

# Calculations
combinded_name = name1 + name2
lowercase_name = combinded_name.lower()

true = lowercase_name.count("t") + lowercase_name.count("r") + \
    lowercase_name.count("u") + lowercase_name.count("e")

love = lowercase_name.count("l") + lowercase_name.count("o") + \
    lowercase_name.count("v") + lowercase_name.count("e")

love_score = int(str(true) + str(love))

# Output
if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score},you go together like coke and mentos")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score},you two are alright together")
else:
    print(f"Your score is {love_score}")
