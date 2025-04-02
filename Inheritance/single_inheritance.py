class Employee:
  def __init__(self,name,salary):
    self.name= name
    self.salary= salary

  def show_detaile(self):
    print(f"Name is: {self.name}")
    print(f"Salary is: {self.salary}")


class Manager(Employee):
    def __init__(self, name, salary,department):
        super().__init__(name, salary)
        self.department= department
        self.tem_size= 5

    def show_detaile(self):
        super().show_detaile()
        print(f"department is: {self.department}")
        print(f"Team size is: {self.tem_size}") 
        

emp1= Manager("Abhinav",150000,"senior programmer")
emp1.show_detaile()
