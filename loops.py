#loops
#for loop
for i in range(5):
    print("Welcome Memona!")



for number in range(1,11):
    print(number)
    for second in range(10,0,-1):
     print(second)
print("Launch!")


for even in range(2,21,2):
    print(even)



for odd in range(1,20,2):
    print(odd)



number = 7
for i in range(1,11):
    print(number,"x",i,"=",number*i)



for number in range(1,11):
    print(number**2)
    


for student_id in range(1001,1011):
    print(student_id)




name = "Memona"
for i in range(5):
    print("Welcome",name)



sentence = "Artificial Intelligence"
for character in sentence:
    print(character)




dream_universities = [
    "MIT",
    "Harvard",
    "Stanford",
    "Oxford"
]
for university in dream_universities:
    print(university)



total = 0
for number in range(1,11):
    total += number
print(total)



total = 0

for even in range(2,21,2):
    total += even
print(total)



salary = 50000
for month in range(1,13):
    salary += 5000
    print("Month",month,"Salary",salary)




count = 0

for number in range(1,21):
    if number % 2 == 0:
        count += 1
print("Even numbers:", count)





number = 5
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print(factorial)



word = "Artificial Intelligence"
count = 0
for letter in word:
    if letter.lower() in "aeiou":
        count += 1
print("Vowels:", count)



marks = [95,88,76,91]
total = 0
for mark in marks:
    total += mark
print(total)




#while loop
count = 0
while count < 5:
    print('welcome memona!')
    count += 1




count = 10
while count >= 1:
    print(count)
    count -= 1
print('Launch!')





number = 1
while number <= 19:
    print(number)
    number += 2




number = 7
i = 1
while i <= 10:
    print(number, "x", i, "=", number * i)
    i += 1




total = 0
number = 1
while number <= 10:
    total += number
    number += 1
print(total)



number = 5
factorial = 1
i = 1
while i <= number:
    factorial *= i
    i += 1
print(factorial)





password = ""
while password != "myty44":
    password = input("Enter password: ")
print("Login Successful!")





balance = 10000
while balance > 0:
    withdraw = int(input("Enter amount: "))
    if withdraw <= balance:
        balance -= withdraw
        print("Remaining Balance:", balance)
    else:
        print("Insufficient Balance")



secret = 7
guess = 0

while guess != secret:
    guess = int(input("Guess the number: "))

print("Correct!")



#break,continue,else


for number in range(1,11):
    if number == 5:
        break
    print(number)




correct_password = "Python123"
while True:
    password = input("Enter password: ")
    if password == correct_password:
        print("Login Successful")
        break
    print("Wrong password")




students = ["Ali", "Sara", "Ahmed", "Memona", "Fatima"]
search = "Memona"
for student in students:
    if student == search:
        print("Student Found")
        break





balance = 5000
while True:
    withdraw = int(input("Enter amount (0 to exit): "))
    if withdraw == 0:
        break
    if withdraw <= balance:
        balance -= withdraw
        print("Remaining:", balance)
    else:
        print("Insufficient balance")




for number in range(1, 11):
    if number == 5:
        continue
    print(number)




sentence = "when the power of love beats the love of power world makes peace"
for letter in sentence:
    if letter == " ":
        continue
    print(letter)




for number in range(1, 6):
    print(number)
else:
    print("Loop Finished")




for number in range(1, 6):
    if number == 3:
        break
    print(number)
else:
    print("Loop Finished")




students = ["Ali", "Sara", "Ahmed"]
search = "Memona"
for student in students:
    if student == search:
        print("Found")
        break
else:
    print("Student Not Found")





count = 1
while count <= 3:
    print(count)
    count += 1
else:
    print("Done")