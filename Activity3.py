class Student:
    species = "human"
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
obj1 = Student("Clark", 11)
obj2 = Student("Nathan", 11)
print("Obj1 is {}".format(obj1.species))
print("Obj2 is {}".format(obj2.species))
print("{} is in {}th grade".format(obj1.name, obj1.grade))
print("{} is in {}th grade".format(obj2.name, obj2.grade))