#conditional statement
age = 12
if age >= 18:
    print("You can vote.")
else:
    print('you cannot vote.')





percentage = 91
if percentage >= 90:
    print("Congratulations! You qualified for the scholarship.")
else:
    print('sorry! you did not qualify for the scholarship.')




level = 30
if level >= 25:
    print("New map unlocked!")
else:
    print('keep playing to unlock new app')




username = input("Username: ")
password = input("Password: ")
if username == "memona" and password == "Python123":
    print("Login Successful")
else:
    print("Invalid username or password try again")




sat = int(input("SAT Score: "))
ielts = float(input("IELTS Score: "))
activities = int(input("Number of Activities: "))
if sat >= 1500 and ielts >= 7.5 and activities >= 5:
    print("Eligible for Admission")
else:
    print("Not Eligible")




total_bill = float(input("Enter Total Bill: "))
if total_bill >= 10000:
    discount = total_bill * 0.20
    final_bill = total_bill - discount
    print("20% Discount Applied")
    print("Discount:", discount)
    print("Final Bill:", final_bill)
else:
    print('no discount applied')
    



marks = int(input('enter your marks:'))
if marks >= 90:
    print("Grade A+")

elif marks >= 80:
    print("Grade A")

elif marks >= 70:
    print("Grade B")

elif marks >= 60:
    print("Grade C")

else:
    print("Fail")




battery = 18
if battery >= 80:
    print("Battery Full")

elif battery >= 50:
    print("Battery ok")

elif battery >= 20:
    print("Battery Low")

else:
    print("Charge Immediately!")




percentage = 93
if percentage >= 95:
    print("100% Scholarship")

elif percentage >= 90:
    print("75% Scholarship")

elif percentage >= 85:
    print("50% Scholarship")

elif percentage >= 80:
    print("25% Scholarship")

else:
    print("No Scholarship")



temperature = 32
if temperature >= 40:
    print("Heat Wave")

elif temperature >= 30:
    print("Hot")

elif temperature >= 20:
    print("Pleasant")

else:
    print("Cold")



    