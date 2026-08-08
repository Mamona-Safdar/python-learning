#TUPLE
info = (
    "Memona",
    18,
    True,
    4.95
)
print(info)


colors = (
    "Red",
    "Blue",
    "Green",
    "Black"
)
print(colors)



#Accessing Tuple Elements

universities = (
    "MIT",
    "Harvard",
    "Stanford",
    "Oxford"
)
print(universities[0])
print(universities[2])
print(universities[-1])
print(universities[-2])
print(universities[1:3])

#Tuple Packing (putting multiple values into one tuple)
student = (
    "Memona",
    18,
    "Pakistan"
)
print(student)


#tuple unpacking
student = (
    "Memona",
    18,
    "Pakistan"
)

name, age, country = student

print(name)
print(age)
print(country)



#Tuple Methods
numbers = (
    10,
    20,
    10,
    30,
    10
)
print(numbers.count(10))


languages = (
    "Python",
    "Java",
    "Go"
)
print(languages.index("Go"))


#Extended Unpacking (*)
subjects = (
    "Math",
    "Physics",
    "Computer",
    "English",
    "Urdu"
)
first, *middle, last = subjects
print(first)
print(middle)
print(last)




numbers = (
    10,
    20,
    30,
    40,
    50
)
first, *others = numbers
print(first)
print(others)




numbers = (
    10,
    20,
    30,
    40,
    50
)
*start, last = numbers
print(start)
print(last)



def rectangle(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter
area, perimeter = rectangle(10, 5)
print(area)
print(perimeter)



#Nested Tuples

students = (
    ("MISHAL", 90),
    ("MINHA", 95),
    ("MEMONA", 99)
)
print(students)


#LIST INSIDE A TUPLE
data = (
    "Python",
    [10, 20, 30]
)
data[1].append(40)
print(data)




#DICT INSIDE A TUPLE
student = (
    "Memona",
    {
        "Math": 95,
        "Physics": 90
    }
)
print(student)


#Looping Through Tuples
languages = ("Python", "Java", "Go")
for language in languages:
    print(language)




marks = (90, 85, 95, 88)
for mark in marks:
    print(mark)




#Using range()
languages = ("Python", "Java", "Go")
for i in range(len(languages)):
    print(i, languages[i])



coordinates = (24.86, 67.00)
for value in coordinates:
    print(value)



#SORTED
numbers = (50, 10, 40, 20)
print(sorted(numbers))



#Converting Between Lists and Tuples
#FROM TUPLE TO LIST]

colors = ("Red", "Blue", "Green")
colors_list = list(colors)
print(colors_list)
print(type(colors_list))




#FROM LIST TO TUPLE
colors = ["Red", "Blue", "Green"]
colors_tuple = tuple(colors)
print(colors_tuple)
print(type(colors_tuple))

#Tuple Concatenation

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print(tuple1 + tuple2)



#Repettion
name = ("memona",)
print(name * 5)


