#Implicit Type Conversion

age = 18
height = 5.7
result = age + height
print(result)
print(type(result))

price = 500
tax = 25.5
total = price + tax
print(total)
print(type(total))

marks = 450
bonus = 2.5
final_marks = marks + bonus
print(final_marks)
print(type(final_marks))

radius = 7
PI = 3.14
area = PI * radius * radius
print(area)
print(type(area))

salary = 50000
increment = 2500.75
new_salary = salary + increment
print(new_salary)
print(type(new_salary))

#Explicit Type Conversion

age = 18
height = 5.7
total = float(age) + height
print(total)

marks = int(input("Enter your marks: "))
print(marks)
print(type(marks))

#ATM System

balance = "25000"
withdraw = 5000
remaining_balance = int(balance) - withdraw
print(remaining_balance)
print(type(remaining_balance))

#Shopping Cart
price = "1500"
quantity = 3
bill = int(price) * quantity
print(bill)

#Age Calculator

birth_year = input("Enter your birth year: ")
current_year = 2026
age = current_year - int(birth_year)
print(age)

#Cricket Match

runs = "245"
extras = 18
total = int(runs) + extras
print(total)

#BMI CALCULATOR

height = input("Enter height in meters: ")
weight = 60
bmi = weight / (float(height) ** 2)
print(bmi)

#student id card

student_id = 20261001
message = "Your ID is: " + str(student_id)
print(message)

#shopping receipt 

bill = 4599.75
receipt = "Total Bill: Rs. " + str(bill)
print(receipt)

balance = 2500
has_money = bool(balance)
print(has_money)