class Calculate:
  def add (self,num1,num2,num3=0,num4=0):
    return num1 + num2 + num3 + num4
  
cal= Calculate()

print(cal.add(5,5))
print(cal.add(5,5,5))
print(cal.add(5,5,5,5))
