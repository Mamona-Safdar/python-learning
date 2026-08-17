class Student:
    def __init__(self):
        pass








class Student:

    def __init__(self, name):
        self.name = name





class CollegeStudent(Student):
          pass
student1 = CollegeStudent("Memona")









class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    def drive(self):
        print("The car is driving")
car1 = Car("Toyota", "Red")
car2 = Car("Honda", "Blue")
print(car1.brand)
car1.drive()







class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print(f"{self.name} says Woof!")

dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)
dog1.bark()
dog2.bark()





class Phone:
    def __init__(self, brand, battery):
        self.brand = brand
        self.battery = battery

    def charge(self):
        self.battery = 100
        print("Phone fully charged")
phone = Phone("Samsung", 40)
print(phone.battery)
phone.charge()
print(phone.battery)






class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def check_result(self):
        if self.marks >= 50:
            print(f"{self.name} passed")
        else:
            print(f"{self.name} failed")
student1 = Student("Memona", 85)
student2 = Student("Sara", 40)
student1.check_result()
student2.check_result()









class Patient:
    def __init__(self, name, age, disease):
        self.name = name
        self.age = age
        self.disease = disease

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Disease: {self.disease}")
patient1 = Patient("Sara", 18, "Fever")
patient2 = Patient("Ayesha", 20, "Flu")
patient1.show_info()
print()
patient2.show_info()






class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self):
        print(f"{self.name} attacks!")
    def take_damage(self, damage):
        self.health -= damage
player = Character("Hero", 100)
player.attack()
player.take_damage(20)
print(player.health)