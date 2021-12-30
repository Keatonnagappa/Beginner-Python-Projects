# User input
age = input("What is your current age?")
age_as_int = int(age)

# Time in 90 years
days_90 = 32850
weeks_90 = 4680
months_90 = 1080

# Calculations
days_alive = age_as_int * 365
weeks_alive = age_as_int * 52
months_alive = age_as_int * 12

days_left = days_90 - days_alive
weeks_left = weeks_90 - weeks_alive
months_left = months_90 - months_alive

# output
print(
    f"You have {days_left} days, {weeks_left} weeks, {months_left} months left.")


# Alternatively I could have used a simpler method as seen below:

# age = input("What is your current age?")
# age_as_int = int(age)

# years_remaining = 90 - age_as_int
# days_remaining = years_remaining * 365
# weeks_remaining = years_remaining * 52
# months_remaining = years_remaining * 12

# message = f"You have {days_remaining} days, {weeks_remaining} weeks, {months_remaining} months left."
# print(message)
