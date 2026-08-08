#functionss
#built in function

students = [
    "Ayan",
    "Shayan",
    "Zadfa",
    "Memona",
    "Fatima"
]
print(len(students))



prompt = input("Enter Prompt: ")
print("Characters:", len(prompt))




cart = [
    "Laptop",
    "Mouse",
    "Keyboard",
    "Monitor"
]
print("Items:", len(cart))




dna = "abbabbbabba"
print(len(dna))



monthly_sales = [
    15000,
    22000,
    31000,
    27000,
    35000
]
print(sum(monthly_sales))




marks = [
    92,
    81,
    99,
    76,
    88
]
print(sorted(marks))



cgpa = 3.87654
print(round(cgpa,2))


salary = 50000
print(type(salary))


#user de4fined functions

def bank_statement():
    print("Bank Name: MCB Bank")
    print("Balance: 250000")
    print("Status: Active")
bank_statement()



def student_report():
    print("Student: Memona")
    print("Department: Computer Science")
    print("CGPA: 4.91")
student_report()




def train_model():
    print("Loading Dataset...")
    print("Training Started...")
    print("Training Complete.")
train_model()


#Parameters & Arguments

#parameter
def greet(name):
    print("Welcome", name)
#arguments
greet("Memona")

#student report card 
def student_report(name, department, cgpa): #parameter
    print("Student:", name)
    print("Department:", department)
    print("CGPA:", cgpa)
student_report("Memona", "Computer Science", 4.91)#argument
student_report("Abdullah", "AI", 3.72)#argument




#Salary Calculator

def yearly_salary(employee, monthly_salary):
    yearly = monthly_salary * 12
    print(employee)
    print("Yearly Salary:", yearly)
yearly_salary("maria", 85000)
yearly_salary("memona", 120000)


def model_report(model_name, accuracy):
    print("Model:", model_name)
    print("Accuracy:", accuracy, "%")
model_report("Random", 94.7)
model_report("XYZ", 97.2)

 
    
def book_ticket(name, destination, seat):
    print("Passenger:", name)
    print("Destination:", destination)
    print("Seat:", seat)
book_ticket("Memona", "us", "12A")
book_ticket("Ali", "uk", "18F")


#Positional Arguments

def student(name, age):
    print(name)
    print(age)
student("Memona", 18)




def login(username, password):
    print("Username:", username)
    print("Password:", password)
login("Memona", "py@123")




def course(name, duration):
    print(name)
    print(duration)
course("Machine Learning", "6 Months")




#Default Arguments

def welcome(name="Guest"):
    print("Welcome", name)
welcome()
welcome("Memona")



def discount(price, discount_percent=10):
    final = price - (price * discount_percent / 100)
    print(final)
discount(5000)
discount(5000, 25)



def send_email(receiver, subject="No Subject"):
    print("To:", receiver)
    print("Subject:", subject)
send_email("memona@email.com")
send_email(
    "memona@email.com",
    "MIT Application"
)


#Keyword Arguments
def employee(name, salary, department):
    print(name)
    print(salary)
    print(department)
employee(
    department="AI",
    salary=120000,
    name="Memona"
)



def flight(name, destination, seat):
    print(name)
    print(destination)
    print(seat)
flight(
    seat="14A",
    destination="London",
    name="Memona"
)



def transfer(sender, receiver, amount):
    print(sender)
    print(receiver)
    print(amount)
transfer(
    amount=5000,
    sender="Memona",
    receiver="zadfa"
)

def transfer(sender, receiver, amount):
    print(sender)
    print(receiver)
    print(amount)

'''sender = input("Enter sender name: ")
receiver = input("Enter receiver name: ")
amount = int(input("Enter amount: "))

transfer(
    sender=sender,
    receiver=receiver,
    amount=amount
)'''

#RETURN STATEMENT

def square(number):
    return number ** 2
result = square(8)
print(result)


def yearly_salary(monthly):
    return monthly * 12
salary = yearly_salary(95000)
print(salary)




def discount(price):
    return price * 10
final_price = discount(25000)
print(final_price)


def area(length, width):
    return length * width
room = area(20,15)
print(room)



def accuracy(correct, total):
    return (correct/total)*100
print(accuracy(940,1000))



#Returning Multiple Values

def student():
    return "Memona",18,"Pakistan"
name,age,country = student()
print(name)
print(age)
print(country)




def login():
    username = "Memona"
    status = True
    return username,status
user,logged = login()
print(user)
print(logged)




def calculate_tax(salary):
    return salary * 0.15
def yearly_salary(monthly):
    return monthly * 12
salary = yearly_salary(95000)
tax = calculate_tax(salary)
print("Yearly Salary:", salary)
print("Tax:", tax)
print("After Tax:", salary-tax)




#LOCAL SCOPE(variable created inside a function exists only inside that function)


def bank_account():
    balance = 25000
    print("Balance:", balance)
bank_account()


def ticket():
    seat = "1A"
    destination = "Dubai"
    print(seat)
ticket()


#GLOBAL SCOPE

university = "MIT"
def student():
    print(university)
student()
print(university)




tax_rate = 0.15
def calculate_tax(salary):
    print(salary * tax_rate)
calculate_tax(500000)



company = "OpenAI"
def employee():
    print(company)
employee()
print(company)



PI = 3.14159
def area(radius):
    print(PI * radius ** 2)
area(8)



#global Keyword

count = 0

def increase():
    global count
    count += 1
increase()
print(count)




visitors = 0
def visit():
    global visitors
    visitors += 1
visit()
visit()
visit()
print(visitors)




temperature = 25
def increase():
    global temperature
    temperature += 5
increase()
print(temperature)




#*args (number of positional arguments into a tuple)

def total(*numbers):
    print(numbers)
total(10,20,30,40)




def total(*numbers):
    print(sum(numbers))
total(10,20)
total(10,20,30)
total(10,20,30,40,50)




def highest(*scores):
    print(max(scores))
highest(78,91,88,95,84)




def average(*marks):
    print(sum(marks)/len(marks))
average(90,91,95,88,84)





#**kwargs(collects keyword arguments into a dictionary)


def student(**details):
    print(details)
student(
    name="Memona",
    age=18,
   city="Okara"
)



def profile(**info):
    for key, value in info.items():
        print(key,":",value)
profile(
    username="Memona",
    followers=240000,
    verified=True
)




def laptop(**specs):
    print(specs)
    laptop(
        brand='lenovo',
        ram='32GB',
        processor='9ryzne'
    )




def employee(**details):
    for key, value in details.items():
        print(key, value)
employee(
    name="Sara",
    department="AI",
    salary=250000
)



#Lambda Functions (nameless function)

bonus = lambda salary: salary * 1.15
print(bonus(120000))



convert = lambda c: (c * 9/5) + 32
print(convert(30))




percentage = lambda obtained, total: (obtained / total) * 100
print(percentage(455, 500))




tax = lambda salary: salary * 0.12
print(tax(250000))



students = [
    ("Ayan",92),
    ("Sara",88),
    ("Memona",99),
    ("Zadfa",81)
]
students.sort(key=lambda student: student[1])
print(students)





#recursion(function that call itself)

def countdown(number):
    if number == 0:
        return
    print(number)
    countdown(number - 1)
countdown(5)




def factorial(number):
    if number == 1:
        return 1
    return number * factorial(number - 1)
print(factorial(5))





def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)
print(power(3,4))








#Decorators
def decorator(function):
    def wrapper():
        print("Before")
        function()
        print("After")
    return wrapper

