# Python function to fing the area of rectangle using constructor and destructor
# Class Rectangle created
class Rectangle:

      # Initializing the rectangle instance
      def __init__ (self,l,b):
           print("Initializing an rectangle instance")
           self.l=l
           self.b=b

      # Calculating the area of rectangle   
      def area_r(self):
            area=self.l*self.b
            print("Area of rectangle is ",area)

      # Destroying the instance of rectangle
      def __del__(self):
         print("Instance is destroyed")

c=Rectangle(15,15)
c.area_r()
c.__del__()
