#DICTIONARY (collection of data stored as key-value pairs)

student = {
    "name": "Memona",
    "age": 18,
    "city": "Okara"
}
print(student)



book = {
    "title": "Python Basics",
    "pages": 350,
    "price": 2500
}
print(book)



car = {
    "brand": "Tesla",
    "model": "Model 3",
    "year": 2024
}
print(car)


data = {
    True: "Yes",
    False: "No"
}
print(data)



user = {
    "username": "jhonshutup",
    "email": "john@gmail.com",
    "password": "njnjqed2"
}
print(user)



player = {
    "health": 100,
    "score": 4500,
    "level": 7
}
print(player)

#DICT METHODS
#Square Brackets[] (inside the brackets you write a KEY to access value)


student = {
    "name": "Memona",
    "age": 18,
    "city": "Okara"
}
print(student["name"])
print(student["age"])
print(student["city"])



fruit = {
    "first": "Apple",
    "second": "Banana",
    "third": "Mango"
}
print(fruit["third"])

#get()
student = {
    "name": "Ali",
    "age": 18
}
print(student.get("name"))



student = {
    "name": "Ali"
}
print(student.get("marks", "Not Available"))



#Updating Values

student = {
    "name": "Memona",
    "age": 18
}
student["age"] = 17
print(student)


laptop = {
    "brand": "Lenovo",
    "price": 180000
}
laptop["price"] = 200000
print(laptop)


account = {
    "username": "Memona",
    "verified": False
}
account["verified"] = True
print(account)



#del()
student = {
    "name":"Ali",
    "age":18
}
del student["age"]
print(student)


#pop()

student = {
    "name":"Ali",
    "age":18
}
student.pop("age")
print(student)



#clear()

student = {
    "name":"Memona",
    "age":18
}
student.clear()
print(student)


#len()

student = {
    "name":"Ali",
    "age":18,
    "city":"Lahore"
}
print(len(student))


#keys() only give keys
#values() only give values

student = {
    "name":"Ali",
    "age":18,
    "city":"Lahore"
}
print(student.values())
print(student.keys())

#items
student = {
    "name":"Ali",
    "age":18,
    "city":"Lahore"
}
print(student.items())

#Looping Through Dictionary

student = {
    "name":"Ali",
    "age":18,
    "city":"Lahore"
}
for key in student:
    print(key)


student = {
    "name":"Ali",
    "age":18,
    "city":"Lahore"
}
for value in student.values():
    print(value)


#looping list in dict
products = [
    {
        "name": "Laptop",
        "price": 120000
    },
    {
        "name": "Mouse",
        "price": 2500
    },
    {
        "name": "Keyboard",
        "price": 6000
    }
]
for product in products:
    print(product["name"])

#enumerate() [gives the index the value]

students = ["Ayyan", "Shayan", "Memona", "Fatima"]
for index, student in enumerate(students):
    print(index, student)


subjects = ["Math", "Physics", "Computer"]
for index, subject in enumerate(subjects):
    print(index, subject)



#Nested Dictionaries

students = {
    "student1": {
        "name": "Memona",
        "age": 18,
        "city": "Okara"
    },
    "student2": {
        "name": "Sara",
        "age": 17,
        "city": "Sahiwal"
    }
}
print(students["student1"]["name"])
print(students["student1"]["age"])
print(students["student2"]["city"])


#Lists Inside Dictionaries

playlist = {
    "name": "My Playlist",
    "songs": [
        "Dai Dai",
        "Espresso",
        "Reflection",
        "Breakin' dishes",
        "Starboy"
    ]
}
print(playlist["songs"][0])
print(playlist["songs"][1])




#Dictionaries Inside Lists

students = [

    {
        "name": "Anaya",
        "age": 18
    },
    {
        "name": "Sara",
        "age": 17
    },
    {
        "name": "Ayesha",
        "age": 19
    }
]
print(students[1]["name"])
print(students[2]["age"])


prediction = {
    "person":"Memona",
    "confidence":98,
    "emotion":"Happy"
}
print(prediction["confidence"])

#json(JavaScript Object Notation) and dict look same

students = [
    {
        "name": "Memona",
        "marks": 95,
        "subjects": ["Math", "Physics"]
    },
    {
        "name": "Maria",
        "marks": 88,
        "subjects": ["Computer", "English"]
    }
]
for student in students:
    print(f"Student: {student['name']}")
    print(f"Marks: {student['marks']}")
    print("Subjects:")

    for subject in student["subjects"]:
        print("-", subject)

    print()


#Dictionary Comprehension (short way to create dictionaries ~
# SYNTAX new_dict = {key: value for item in iterable})
#IF CONDITION new_dict = {key: value for item in iterable if condition}

squares = {num: num ** 2 for num in range(1, 6)}
print(squares)


cubes = {num: num ** 3 for num in range(1, 6)}
print(cubes)



students = ["Ali", "Sara", "Ahmed", "Memona"]
marks = {student: 90 for student in students}
print(marks)




prices = {
    "Laptop": 200000,
    "Phone": 120000,
    "Tablet": 80000
}
taxed = {
    item: price * 1.18
    for item, price in prices.items()
}
print(taxed)


#Dictionary Comprehension with if-else

marks = {
    "Ali": 85,
    "Sara": 96,
    "Ahmed": 72,
    "Memona": 99
}
top_students = {
    name: mark
    for name, mark in marks.items()
    if mark >= 90
}
print(top_students)



status = {
    num: "Even" if num % 2 == 0 else "Odd"
    for num in range(1, 6)
}
print(status)



#fromkeys() Creates a dictionary quickly
keys = ["Math","Physics","CS"]
marks = dict.fromkeys(keys,0)
print(marks)


#setdefault() if key exists return its value if doesn't exist create it with a default value and return

student = {
    "name": "Memona",
    "age": 18
}
result = student.setdefault("city", "Okara")
print(result)
print(student)



#Sorted Dictionary

student = {
    "c":3,
    "a":1,
    "b":2
}
print(sorted(student))



#deepcopy() creates a completely independent copy of an object

import copy
original = [10, 20, 30]
new_list = copy.deepcopy(original)
new_list.append(40)
print(original)
print(new_list)


import copy

original = [
    [1, 2],
    [3, 4]
]
new_list = copy.deepcopy(original)
new_list[0][0] = 100
print(original)
print(new_list)


#shallow copy (Creates a new outer object, but nested objects are still shared with the original)
data = [
    [10, 20],
    [30, 40]
]
copy_data = data.copy()
copy_data[0] = ["Python", "AI"]
print(data)
print(copy_data)



#Merge Dictionaries

student = {
    "name": "Ali"
}
extra = {
    "age": 18
}
result = student | extra
print(result)



profile = {
    "username": "memona_ai",
    "followers": 500
}
# Add new info
profile.update({"bio": "Learning Python"})
# Make a backup
backup = profile.copy()
# Ensure website has a country
profile.setdefault("country", "Pakistan")
print(profile)
print(backup)



#IN operator checks whether a key exists in a dictionary
if "bio" in profile:
    print(profile["bio"])
else:
    print("No bio")



#popitem() Removes the last inserted key-value pair
student = {
    "name":"Ali",
    "age":18,
    "city":"Lahore"
}
removed = student.popitem()
print(removed)
print(student)


#assignment =
student = {
    "name":"Ali"
}
student2 = student
student2["name"] = "Sara"
print(student)
print(student2)


#Mutable vs Immutable Keys
#dict are mutable
#dict keys are are immutable
#Hash Table (super-fast storage system for dictionaries)



#Frequency Counter (counts how many times each item appears)


fruits = [
    "apple",
    "banana",
    "apple",
    "mango",
    "banana",
    "apple"
]
frequency = {}
for fruit in fruits:
    if fruit in frequency:
        frequency[fruit] += 1
    else:
        frequency[fruit] = 1
print(frequency)





grades = [
    "A",
    "B",
    "A",
    "C",
    "B",
    "A",
    "A"
]
frequency = {}
for grade in grades:
    if grade in frequency:
        frequency[grade] += 1
    else:
        frequency[grade] = 1
print(frequency)




#short way get()

numbers = [1,2,1,3,2,1]
frequency = {}
for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1
print(frequency)




#Dictionary Unpacking (**) take the key-value pairs out of a dictionary and use them individually
#*   → Used for lists and tuples
#**  → Used for dictionaries

a = {
    "x":1
}
b = {
    "y":2
}
c = {
    "z":3
}
result = {
    **a,
    **b,
    **c
}
print(result)




basic = {
    "name":"Memona"
}
extra = {
    "country":"Pakistan"
}
social = {
    "github":"memona-safdar"
}
profile = {
    **basic,
    **extra,
    **social
}
print(profile)





from collections import Counter
word = "banana"
count = Counter(word)
print(count)



#Counter Methods

#elements()

from collections import Counter
c = Counter("banana")
print(list(c.elements()))



#defaultdict()

from collections import defaultdict
marks = defaultdict(int)
marks["Ali"] += 1
print(marks)




