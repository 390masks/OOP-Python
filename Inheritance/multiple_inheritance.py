class Employee:
    def __init__(self,name,salary):
        self.name= name
        self.salary=salary

    def show_detaile(self):
        print(f"Name is: {self.name}")
        print(f"Salary is: {self.salary}")

class Department:
    def __init__(self,department):
        self.department= department

    def show_department(self):
        print(f"Department is: {self.department}")

class Manager(Employee,Department):
    def __init__(self, name, salary,department,team_size):
        Employee.__init__(self,name,salary)
        Department.__init__(self,department)
        self.team_size=team_size

    def show_detaile(self):
         super().show_detaile()
         print(f"Department is : {self.department}")
         print(f"Team size is : {self.team_size}")

emp1 = Manager("Abhinav", 150000, "Senior Programmer", 5)
emp1.show_detaile()
