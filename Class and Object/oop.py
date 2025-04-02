#creating class , calss is like a blue print 
class Bike:
  #Constructor
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year= year 
    #difine method to display details
    def display_details(self):
        print(f"Bike Brand is: {self.brand}")
        print(f"Bike model is: {self.model}")
        print(f"year is: {self.year}")
# Creating an object (instance of Car)
b1=Bike("Fz","V2",2017)
#calling the method 
b1.display_details()
