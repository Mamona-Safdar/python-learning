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

