# input
print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
tip_percentage = int(input(
    "What percentage tip would you like to give? 10, 12 or 15?"))
bill_split = int(input("How many people to split the bill? "))

# Calculation
bill_with_tip = (tip_percentage / 100) * bill + bill

final_answer = bill_with_tip / bill_split

final_answer_rounded = round(final_answer, 2)

# Enforcing 2 decimal points
final_answer_rounded = "{:.2f}".format(final_answer_rounded)

# Output
print(f"Each person should pay: ${final_answer_rounded}")
