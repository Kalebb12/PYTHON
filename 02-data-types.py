# # 1st input: enter height in meters e.g: 1.65
# height = input()
# # 2nd input: enter weight in kilograms e.g: 72
# weight = input()
# # 🚨 Don't change the code above 👆

# # Write your code below this line 👇
# int_weight = int(weight)
# float_height = float(height)

# bmi = int_weight / float_height ** 2
# print(int(bmi))

# print(4 // 2)

# score = 0

# user scores a point
# score += 1

# f-string
# print(f"Your score is {score}")

print("Welcome to the tip calculator")
bill = input("what was the totat bill? $")
tip = input("How much tip would you like to give? ")
people = input("How many people to split the bill? ")


tip_as_percent = int(tip) / 100
total_tip = float(bill) * tip_as_percent
total_bill = float(bill) + total_tip

split_bill = total_bill / int(people)

print(f"Each person should pay: ${round(split_bill , 2)}")