#arthmetic operators

programming = 92
database = 88
networking = 91
ai = 95
total_marks = programming + database + networking + ai
print("Total Marks:", total_marks)
print(type(total_marks))


monday_sales = 1000
tuesday_sales = 90000
wednesday_sales = 16000
weekly_sales = monday_sales + tuesday_sales + wednesday_sales
print("Total Revenue:", weekly_sales)

morning_patients = 38
afternoon_patients = 45
evening_patients = 29
total_patients = morning_patients + afternoon_patients + evening_patients
print("Total Patients:", total_patients)


match1_runs = 275
match2_runs = 310
match3_runs = 289
total_runs = match1_runs + match2_runs + match3_runs

print("Total Runs:", total_runs)


income = 120000
expenses = 76000
savings = income - expenses
print(savings)


monthly_fee = 2800
months = 12
annual_fee = monthly_fee * months
print(annual_fee)


internet_data = 100
days = 30
daily_usage = internet_data / days
print("Daily Internet Usage:", daily_usage)


guests = 93
room_capacity = 2
full_rooms = guests // room_capacity
print(full_rooms)


files = 1050
disk = 128
remaining = files % disk
print(remaining)

growth_factor = 2
future_growth = growth_factor ** 10
print(future_growth)


#Assignment Operators

balance = 25000
deposit = 5000
balance += deposit
print(balance)


score = 150
bonus = 50
score += bonus
print(score)

savings = 120000
monthly_save = 18000
savings += monthly_save
print(savings)


battery = 100
battery -= 25
print(battery)

marks = 500
lost_marks = 32
marks -= lost_marks
print(marks)

production = 450
days = 30
production *= days
print(production)


investment = 10000
growth_factor = 3
investment *= growth_factor
print(investment)

hotel_bill = 45000
friends = 6
hotel_bill /= friends
print(hotel_bill)



books = 290
days = 7
books //= days
print(books)

pizza_slices = 400
pizza_slices %= 8
print(pizza_slices)

math_value = 20
math_value **= 9
print(math_value)

#comparison operators

entered_pin = 1234
saved_pin = 1234
print(entered_pin == saved_pin)


entered_password = "django1234"
correct_password = "Python123"
print(entered_password != correct_password)

marks = 91
class_average = 74
print(marks > class_average)

password_length = 10
print(password_length >= 8)

#Logical Operators

sat_score = 1510
ielts = 8.0
eligible = sat_score >= 1500 and ielts >= 7.5
print(eligible)

email_correct = False
phone_correct = True
login_success = email_correct or phone_correct
print(login_success)

premium_user = False
free_trial = True
can_watch = premium_user or free_trial
print(can_watch)

game_over = False
continue_playing = not game_over
print(continue_playing)

sat_score = 1520
ielts = 8.0
interview_passed = True
admitted = (sat_score >= 1500 and ielts >= 7.5) or interview_passed
print(admitted)


wallet = 7000
coupon = True
can_buy = wallet >= 8000 or coupon
print(can_buy)

#Identity Operators

student1_marks = 95
student2_marks = 96
print(student1_marks == student2_marks)
print(student1_marks is student2_marks)

file = None
if file is None:
    print("No file uploaded.")


age = 16

if age == 18:
    print("Adult")
else: 
    print('minor')

#Membership Operators

email = "memona@gmail.com"
print("@" in email)


dream_universities = [
    "MIT",
    "Harvard",
    "Stanford",
    "Oxford"
]
print("nus" in dream_universities)

languages = [
    "Python",
    "C++",
    "Java",
    "JavaScript"
]
print("" in languages)

#Operator Precedence (using different operators in an expression)

result = 10 + 5 * 2
print(result)

laptop = 80000
mouse = 2500
quantity = 26
bill = laptop + mouse * quantity
print(bill)


salary = 50000
bonus = 5000
total = (salary + bonus) * 2
print(total)

phone = 95000
cover = 2000
discount = 5000
final_bill = phone + cover - discount
print(final_bill)

