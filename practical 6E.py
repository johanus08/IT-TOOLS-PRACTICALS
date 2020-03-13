# Creating parent class
# Class Parent created
class Parent:
 
    def func1(self):
        print("This is function one")

# Class Child created
class Child(Parent):
    def func2(self):
        print("This is function two")

# Class Child1 created
class Child1(Parent):
    def func3(self):
        print("This is function three")

# Class Child# created
class Child3(Child,Child1):
    def func4(Self):
        print("This is function four")

obj=Child3()
obj.func2()
