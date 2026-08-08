students = [
    "Memona",
    "Ali",
    "Sara",
    "Ahmed",
    "Fatima"
]
print(students)




profile = [
    "Memona",
    18,
    "Pakistan",
    True,
    3.92
]
print(profile)


#Accessing List Elements

students = [
    "Memona",
    "Ali",
    "Sara",
    "Ahmed",
    "Fatima"
]
print(students[0])



scores = [
    88,
    91,
    95,
    84,
    99
]
print(scores[4])


#Negative Indexing
students = [
    "Memona",
    "Ali",
    "Sara",
    "Ahmed",
    "Fatima"
]
print(students[-1])



marks = [
    75,
    82,
    96,
    91,
    88
]
print(marks[-3])
print(marks[-4])



#List Slicing
students = [
    "Memona",
    "Ali",
    "Sara",
    "Ahmed",
    "Fatima"
]
print(students[1:4])
print(students[3:5])


#list methods 

#append


students = [
    "Ali",
    "Sara"
]
students.append("Memona")
print(students)



marks = [
    88,
    91
]
marks.append(95)
print(marks)



#insert

students = [
    "Ali",
    "Sara"
]
students.insert(1, "Memona")
print(students)



numbers = [
    10,
    20,
    40
]
numbers.insert(2, 30)
print(numbers)



#extend()

students = [
    "Ali",
    "Sara"
]
students.extend([
    "Memona",
    "Ahmed"
])
print(students)



numbers = [
    10,
    20
]
numbers.extend([
    30,
    40,
    50
])
print(numbers)



#remove()

students = [
    "Ali",
    "Sara",
    "Memona"
]
students.remove("Sara")
print(students)



numbers = [
    10,
    20,
    30
]
numbers.remove(20)
print(numbers)



#pop()

students = [
    "Ali",
    "Sara",
    "Memona"
]
students.pop()
print(students)


numbers = [
    10,
    20,
    30
]
numbers.pop(1)
print(numbers)



#clear()

students = [
    "Ali",
    "Sara",
    "Memona"
]
students.clear()
print(students)



cities = ["Lahore", 
          "Karachi"
]
cities.clear()
print(cities)


#delete


students = [
    "Ali",
    "Sara",
    "Memona",
    "Ahmed"
]
del students[1:3]
print(students)



cities = [
    "Lahore",
    "Karachi"
]
del cities



#Concatenation(joining two or more lists)
python_topics = [
    "Variables",
    "Functions"
]
advanced_topics = [
    "Lists",
    "Tuples"
]
course = python_topics + advanced_topics
print(course)



morning_tasks = [
    "Study",
    "Exercise"
]
evening_tasks = [
    "Coding",
    "Reading"
]
day_plan = morning_tasks + evening_tasks
print(day_plan)



#Repetition (*)
numbers = [10, 20]
print(numbers * 3)



letters = ["A", "B", "C"]
print(letters * 4)




#Membership Operators

marks = [
    80,
    90,
    100
]
print(95 in marks)



students = [
    "Ali",
    "Sara",
    "Memona"
]
print("Memona" in students)

#not in
cities = [
    "Lahore",
    "Karachi"
]
print("Islamabad" not in cities)



numbers = [
    5,
    10,
    15
]
print(20 not in numbers)



#Looping Through a List
students = [
    "Ali",
    "Sara",
    "Memona"
]
for student in students:
    print(student)



#Using range() with Indexes

students = [
    "Ali",
    "Sara",
    "Memona"
]
for index in range(len(students)):
    print(index, students[index])



#nested list(a list that contains other lists)

students = [
    ["Ayesha", 90],
    ["Sara", 95],
    ["Memona", 99]
]
print(students)
print(students[0][0])#if u only want ayesha



products = [
    ["Laptop", 180000],
    ["Phone", 95000],
    ["Tablet", 65000]
]
print(products[0][0])
print(products[1][0])
print(products[2][0])



students = [
    ["Ali", 90],
    ["Sara", 95],
    ["Memona", 99]
]
students[1][1] = 100 #updating values
print(students)


#loop through nested list 
students = [
    ["Mishal", 90],
    ["Minha", 95],
    ["Memona", 99]
]
for student in students:
    print(student)




#Nested Loop (print each value separately.)

students = [
    ["Mishal", 90],
    ["Minha", 95],
    ["Memona", 99]
]
for student in students:
    for value in student:
        print(value)




employees = [
    ["Essa", "HR"],
    ["Asjad", "IT"],
    ["Fatima", "Finance"]
]
for employee in employees:
    print(employee[0], "-", employee[1])





#ALIASING (one list two variables)
numbers1 = [10, 20, 30]
numbers2 = numbers1
numbers2.append(40)
print(numbers1)



list1 = ["Python", "Java", "C++"]
list2 = list1
list2[0] = "Go"
print(list1)
print(list2)




shopping1 = [
    "maskara",
    "lip gloss"
]
shopping2 = shopping1
shopping2.remove("maskara")
print(shopping1)




#COPYING

list1 = [
    "lip gloss",
    "maskara",
    "lip liner"
]
list2 = list1.copy()
list2[0] = "Go"
print(list1)
print(list2)



numbers1 = [10, 20]
numbers2 = numbers1.copy()
numbers2.append(30)
print(numbers1)
print(numbers2)


#DEEP COPY

import copy

# A nested list (a list inside a list)
original_list = [[1, 2, 3], [4, 5, 6]]

# Create a true, 100% independent clone
independent_copy = copy.deepcopy(original_list)

# Change a nested number in the copy
independent_copy[0][0] = 99

# Look at the results
print("Original:", original_list)    # Output: [[1, 2, 3], [4, 5, 6]] (Untouched!)
print("Copy:", independent_copy)       # Output: [[99, 2, 3], [4, 5, 6]] (Modified!)




import copy

# A nested list (a list inside a list)
original = ["apple", ["pizza", "burger"]]

# Create a shallow copy
sauce_copy = original.copy() 

# 1. Changing the top-level structure
sauce_copy.append("banana")
print(original)    # Output: ['apple', ['pizza', 'burger']]
print(sauce_copy)  # Output: ['apple', ['pizza', 'burger'], 'banana']
# Result: The original list did NOT get the banana. They are separate outer containers.

# 2. Changing a nested structure
sauce_copy[1].append("pasta")
print(original)    # Output: ['apple', ['pizza', 'burger', 'pasta']]
print(sauce_copy)  # Output: ['apple', ['pizza', 'burger', 'pasta'], 'banana']