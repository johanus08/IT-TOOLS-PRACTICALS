# Python program to perform arithmetic operations
class Arithmetic_oprt:
    
    # Defining function for calculations
    def calculations(self,number1,number2):
        print(f"The addition of the numbers is :{number1 + number2}")
        print(f"The subtraction of the numbers is :{number1 - number2}")
        print(f"The multiplication of the numbers is :{number1 * number2}")
        print(f"The division of the numbers is :{number1 / number2}")
        print(f"The modulus division of the numbers is:{number1 %number2}")
        print(f"The value of number 1 raised to number2 is {number1 ** number2}")
        print(f"The value of integer division of the numbers is {number1 // number2}")

# Calling object 
a1 = Arithmetic_oprt()
a1.calculations(int(input("Enter number1:")),int(input("Enter number2:")))
