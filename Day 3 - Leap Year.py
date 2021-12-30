# Prompt for input
year = int(input("Which year do you want to check? "))

# Calculations
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not a Leap Year")
    else:
        print("Leap year")
else:
    print("Not a Leap Year")
