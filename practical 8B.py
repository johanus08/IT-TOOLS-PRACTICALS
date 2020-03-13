# Python program
# To overload an binary + operator
# Class a created
class A:
     
     def __init__(self,a):
          self.a=a

     # Adding two objwcts
     def __add__(self,o):
          return self.a+o.a

object1=A(1)
object2=A(2)
object3=A("FY")
object4=A("IT")

print(object1 + object2)
print(object3 + object4)
