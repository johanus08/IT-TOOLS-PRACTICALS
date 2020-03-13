# Class employee created
class Employee:
   
     # Function to calculate salary and incentive.
     def add(self,salary,incentive):
          print(f"Total salary of the base class is {salary + incentive}.")

# Class department created
class Department(Employee):
     
     temp = "I am a member of the department class."
     
     # Function to calculate salary and incentive
     def add(self,salary,incentive):
          print(f"Total salary of the derived class is {salary + incentive}.")
          super(Department,self).add(salary,incentive)

# Class objects created.
dept = Department()
dept.add(45000,5000)
