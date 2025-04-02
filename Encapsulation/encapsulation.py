class BanckAccount:
    def __init__(self,ac_number,balance):
            self.account_number= ac_number
            self._bank_name="SBI"
            self.__balance=balance
    def deposite(self,amount):
          self.__balance += amount
          print(f"Deposited amount is: {amount} \n New balance is: {self.__balance}")
    
    def withdraw(self,amount):
        if amount <= self.__balance:
                self.__balance -= amount
                print(f"withdraw amount is: {amount} \n New balance is: {self.__balance}")
        else:
             print("Insufficient balance!")
    def check_balance(self):
          return self.__balance
    

ac1= BanckAccount("257874651676",1000)
print(ac1.account_number)
print(ac1._bank_name)

# Will get an error because it's a private attribute
# print(ac1.__balance)

ac1.deposite(5000)
print(ac1.check_balance())

ac1.withdraw(1000)
print(ac1.check_balance())
