class AutoInsurance:
  def __init__(self,policy_number,premium):
    self.policy_number = policy_number
    self._premium = premium

  @property
  def premium(self):
    return self._premium
  
  @premium.setter
  def premium(self,amount):
    if amount < 0:
      raise ValueError ("premium cannot be less than zero")
    self._premium = amount

insurance = AutoInsurance("Ai00235",1500)
print(insurance.premium)
insurance.premium = 2000

print(insurance.premium)
