#SET
languages = {"Python", "Java", "Go"}
print(languages)


numbers = {10, 20, 30, 40}
print(numbers)


cities = {"Lahore", "Karachi", "Islamabad"}
print(cities)


students = {
    "Ali",
    "Sara",
    "Ali",
    "Ahmed",
    "Sara"
}
print(students)

#Duplicate Values
numbers = {10, 20, 10, 30, 20}
print(numbers)


letters = {"A", "A", "B", "C", "B"}
print(letters)


#empty set

empty = {}
print(type(empty))#empty dict

empty = set()
print(type(empty))#empty list


languages = {
    "Python",
    "Java",
    "Go"
}
print(len(languages))


#Membership Operators
languages = {
    "Python",
    "Java",
    "Go"
}
print("Python" in languages)


#loop through set
languages = {
    "Python",
    "Java",
    "Go"
}
for language in languages:
    print(language)





#set methods
languages = {"Python", "Java"}
languages.add("Go")
print(languages)



languages = {"Python"}
languages.update(["Java", "Go"])
print(languages)



languages = {"Python", "Java", "Go"}
languages.remove("Java")
print(languages)



languages = {"Python", "Java"}
languages.discard("Java")
print(languages)


languages = {"Python", "Java"}
languages.discard("C++")
print(languages)#no error if value present removes it no chngs




languages = {
    "Python",
    "Java",
    "Go"
}
removed = languages.pop()
print(removed)
print(languages)


languages = {
    "Python",
    "Java",
    "Go"
}
languages.clear()
print(languages)




set1 = {
    "Python",
    "Java"
}
set2 = set1.copy()
print(set2)


#union (|)
ai_club = {"Ali", "Sara", "Ahmed"}
robotics_club = {"Sara", "Bilal", "Fatima"}
all_students = ai_club | robotics_club
print(all_students)


colors1 = {"Red", "Blue"}
colors2 = {"Green", "Blue"}
print(colors1 | colors2)



#intersection(&)


ai_club = {
    "Ali",
    "Sara",
    "Ahmed"
}
robotics_club = {
    "Sara",
    "Ahmed",
    "Bilal"
}
print(ai_club & robotics_club)


colors1 = {"Red", "Blue"}
colors2 = {"Blue", "Black"}
print(colors1 & colors2)





#differences(-)


ai_club = {
    "Ali",
    "Sara",
    "Ahmed"
}
robotics_club = {
    "Sara",
    "Bilal"
}
print(ai_club - robotics_club)



english = {"Ali", "Sara", "Ahmed"}
math = {"Sara"}
print(english - math)


#SYMMETRIC DIFFERENCE (^) Return elements that are in either set, but not both

ai_club = {
    "Ali",
    "Sara",
    "Ahmed"
}
robotics_club = {
    "Sara",
    "Bilal"
}
print(ai_club ^ robotics_club)



colors1 = {"Red", "Blue"}
colors2 = {"Blue", "Black"}
print(colors1 ^ colors2)