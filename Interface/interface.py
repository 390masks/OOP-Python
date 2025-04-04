from abc import ABC , abstractmethod

class Payment(ABC):
  
  @abstractmethod
  def initiate_payment(self,amount,recipient):
    pass
  
  @abstractmethod
  def refund_payment(self,transaction_id,amount):
    pass
  
class UPIPaymentGateway(Payment):
  def initiate_payment(self, amount, recipient):
   
    return f"payment amount of RS{amount} , Recipient name is {recipient}"
  
  def refund_payment(self, transaction_id, amount):
    
    return f"Amount refunded RS{amount} and the Transaction ID is: {transaction_id}"
  
class CardPaymentGateway(Payment):
  def initiate_payment(self, amount, card_details):
     
     return f"Amount paid thourgh card RS{amount} card number: {card_details}"
  
  def refund_payment(self, transaction_id, amount):
    
    return f"Amount refunded RS{amount} and the Transaction ID is: {transaction_id}"
  

def process_payment(gateway,amount,recipient):
  result=gateway.initiate_payment(amount,recipient)
  print(result)

upi= UPIPaymentGateway()
process_payment(upi,5000,"Abhinav")

card= CardPaymentGateway()
process_payment(card,10000,"656965677977466")
