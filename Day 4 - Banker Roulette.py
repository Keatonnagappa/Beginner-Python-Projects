import random

# Split string method
names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ")

# Randomizing
winner = random.choice(names)

# Output
print(f"{winner} is going to buy the meal today!")


# Alternatively You could use the below code:
# import random
# Split string method
#names_string = input("Give me everybody's names, seperated by a comma. ")
#names = names_string.split(", ")

# num_items = len(names)
# winner = random.randint(0, num_items - 1)
# person_who_will_pay = names[winner]
# print(f"{person_who_will_pay} is going to buy the meal today!")
