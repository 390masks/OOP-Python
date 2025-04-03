class BankAccount:
   def __init__(self,name,balance):
      self.name= name
      self.balance= balance
    
   def show_details(self):
      print(f"name: {self.name} balance: {self.balance}")

   def __add__(self,other):
      if isinstance(other,BankAccount):
         total_balance = self.balance + other.balance
         return BankAccount(self.name, total_balance)
      
   def __sub__(self,other):
      if isinstance(other,(int,float)):
         total_balance = self.balance - other
         return BankAccount(self.name , total_balance)


   def __str__(self):
      return f"Name: {self.name} , balance: {self.balance}"

account1= BankAccount("Rajeev",1000)
account2= BankAccount("Rajeev",500)

combined_account = account1 + account2
new_balance = combined_account- 200


print(combined_account)
print(new_balance)
