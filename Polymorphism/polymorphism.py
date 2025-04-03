class Shape:
  def perimeter (self):
    pass
  
class Circel(Shape):
    def __init__(self,radius):
        super().__init__()
        self.radius= radius
    def perimeter(self):
        return round(2 * 3.14 * self.radius, 2 )
    
class Rectangle(Shape):
   def __init__(self,length,width):
      super().__init__()
      self.length= length
      self.width= width
   def perimeter(self):
      return 2 * (self.length + self.width)
   
class Triangle(Shape):
   def __init__(self,side1,side2,side3):
      super().__init__()
      self.side1= side1
      self.side2= side2
      self.side3= side3
   def perimeter(self):
      return self.side1 + self.side2 + self.side3
   
def perimeter(shape):
   print(f"Perimeter is: {shape.perimeter()}")

circle= Circel(5)
rectangel= Rectangle(5,10)
triangle=Triangle(5,10,15)

perimeter(circle)
perimeter(rectangel)
perimeter(triangle)
