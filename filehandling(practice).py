
'''word = input("enter a letter:")
vowel = "aeiou"
if word.lower() in vowel:
    print("vowel")
else:
    print("consonant")'''



#find largest number
'''i = (1,2,3,4,5,6,7,8)
for i in range(9):
     if i >= 8:
      print(f"the greatest number is {i}")'''



numbers = [10, 20]
print(numbers * 3)



numbers = [
    5,
    10,
    15
]
print(20 not in numbers)




students = [
    "Ali",
    "Sara",
    "Memona"
]
for index in range(len(students)):
    print(index, students[index])




students = [
    ["Mishal", 90],
    ["Minha", 95],
    ["Memona", 99]
]
for student in students:
    for value in student:

      print(value)




meetings = (
    ("9:30", "10:50"),
    ("9:30", "10:50"),
    ("2:50", "3:50"),
    ("8:00", "9:50")
)
common = set(meetings) & set(meetings)
print(meetings)




students = [
    "Memona",
    "Ali",
    "Sara",
    "Ahmed",
    "Fatima"
]
print(students[1:4])
print(students[3:5])

