class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"Hi, I'm {self.name}, I'm {self.age} years old, and I'm studying {self.course}.")

# Creating three student objects
student1 = Student("Trishia", 23, "Information Technology")
student2 = Student("Sheryn", 22, "Nursing")
student3 = Student("Macy", 20, "Tourism Management")

# Calling their introduce() method
student1.introduce()
student2.introduce()
student3.introduce()