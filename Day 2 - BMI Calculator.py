height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

# BMI Formula
bmi = float(weight) / (float(height)**2)
# output
print(int(bmi))
