from abc import ABC , abstractmethod

class Employee(ABC):
  def __init__(self,name,emp_id):
    super().__init__()
    self.name= name
    self.emp_id = emp_id

  @abstractmethod
  def calculate_salary(self):
    pass
  
  @abstractmethod
  def show_full_info(self):
    pass
  
  def show_basic_info(self):
    return f"name is: {self.name} , ID: {self.emp_id}"
  
class FullTimeEmployee(Employee):
  def __init__(self, name, emp_id,salary):
    super().__init__(name, emp_id)
    self.salary=salary
  
  def calculate_salary(self):
    return f"salary : {self.salary}"
  
  def show_full_info(self):
    return f"name: {self.name} , ID: {self.emp_id} , salary: {self.salary}"
  
class PartTimeEmployee(Employee):
    def __init__(self, name, emp_id,hourly_wage,hours_worked):
      super().__init__(name, emp_id)
      self.hourly_wage = hourly_wage
      self.hours_worked= hours_worked

    def calculate_salary(self):
      total_salary= self.hourly_wage * self.hours_worked
      return f"Total salary: {total_salary}"
    
    def show_full_info(self):
      return f"name: {self.name} , ID : {self.emp_id} salary: {self.hourly_wage}"
    

full_time_employee = FullTimeEmployee("Abhi","01",150000)
print(full_time_employee.calculate_salary())
print(full_time_employee.show_full_info())
print(full_time_employee.show_basic_info())

print("___________________________________________________")

part_time_employee= PartTimeEmployee ("sajith", "02",100, 6 )
print(part_time_employee.calculate_salary())
print(part_time_employee.show_full_info())
print(part_time_employee.show_basic_info())
