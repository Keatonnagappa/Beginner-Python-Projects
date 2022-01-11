# 🚨 Don't change the code below 👇
student_heights = input(
    "Input a list of student heights seperated by spaces: ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

# adding height values using a for loop
total_height = 0
for height in student_heights:
    total_height += height

# Getting the amount of inputs using a for loop
number_of_students = 0
for student in student_heights:
    number_of_students += 1

# Calculations
average_height = round(total_height / number_of_students)

# Output
print(average_height)
