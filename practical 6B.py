# To implement multi-level inheritance
# This class will accept the details of the student.
class Student:
     

     # This method will accept the details of the student.
     def _accept_details_of_the_student(self):
          self.division = input("Enter the division: ")
          self.roll_no = int(input('Enter your roll number: '))
          self.semester = input("Enter your current semester: ")

# This class will accept the marks of the student.
class Marks(Student):
     
     # This method will accept the marks of the student.
     def _accept_marks(self):
          subjects = ['DM','WP','OOP','DBMS','PP']
          self.marks = []  # Contains the marks.
          for subject in subjects:
               self.marks.append(int(input(f"Enter marks for {subject} out of 100: ")))
               
# This class will calculate the total marks of the student.
class Total_percentage(Marks):
    
     # This method will display the total marks and the percentage.
     def _display_total_marks_and_percentage(self):
          print(f"The total marks obtained is {sum(self.marks)}.")
          print(f"The total percentage obtained is {sum(self.marks)/500 * 100}.")

student_details = Total_percentage()  # Object for calling all the methods.
student_details._accept_details_of_the_student()
student_details._accept_marks()
student_details._display_total_marks_and_percentage()     
    
