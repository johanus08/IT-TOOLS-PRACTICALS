# Class property function created
class property_function_demo:
    
     # Initializing the function
     def __init__(self):
          self._age = 0

     # Fucntion for printing the age
     def get_age(self):
         print("Getter method called")
         return self._age

     # Function for setting the age
     def set_age(self,age):
          print("setter method called")

     # Function for deleting the age
     def delete_age(self):
          del self.age

     age = property(get_age,set_age)

object1 = property_function_demo()
object1.age = 10
print(object1.age)
