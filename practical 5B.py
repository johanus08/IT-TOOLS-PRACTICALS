#Python program showing use of @ property decorator
class property_fun_demo:
     
     # Funtion to initialize the age attribute
     def __init__(self):
          self.age = 0

     @property
     
     # A getter function
     def age(self):
          print("Getter method called.")
          return self._age

     @age.setter
     
     # A setter method 
     def age(self,age):
          if(age < 18):
               raise ValueError('Sorry your age is elow the eligibility criteria')
          print("Setter method is called")
          self._age = age

mark = property_fun_demo()  # Object being created 

mark.age = 19
print(mark.age)
