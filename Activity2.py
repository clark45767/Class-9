class Student:
    grade = 11
    name = "Clark"

    def intro(self):
        print("Hi,I am from UAE")

    def details(self):
        print("My name is", self.name)
        print("My grade is : ", self.grade)
obj1 = Student()
obj1.intro()
obj1.details()