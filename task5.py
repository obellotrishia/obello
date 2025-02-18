class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount
        print(f"Salary increase by {amount}. New salary: {self.salary}")

    def display_employee(self):
      print(f"Employee Name: {self.name}")
      print(f"Position: {self.position}")
      print(f"Salary: {self.salary}")