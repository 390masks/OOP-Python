class Employee:
    def __init__(self,name,salary):
        self.name= name
        self.salary= salary

    def show_details(self):
        print(f"name is: {self.name}")
        print(f"salary is: {self.salary}")

class Manager(Employee):
    def __init__(self, name, salary,department):
        super().__init__(name, salary)
        self.department = department
    def show_details(self):
         super().show_details()
         print(f"department is: {self.department}")

class SeniorManager(Manager):
    def __init__(self, name, salary, department,team_size):
        super().__init__(name, salary, department)
        self.team_size= team_size
    def show_details(self):
         super().show_details()
         print(f"team size: {self.team_size}")


emp1=SeniorManager("Abhi",900000,"IT",5)
emp1.show_details()
