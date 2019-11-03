# Name: Abdul Malik 
# Email: abdulmalik422@gmail.com

# Program 1:
print('1) Write a Python program to print the following string in a specific format:')
print('Twinkle, twinkle, little star, \n\t How I wonder what you are! \n\t\t Up above the world so high, \n\t\t Like a diamond in the sky. \n Twinkle, twinkle, little star, \n\t How I wonder what you are')

print('\n\n')

# Program 2:
print('2) Write a Python program to get the Python version you are using:')
import sys  
print('Python Version is: ' + sys.version);


print('\n\n')

# Program 3:
print('3) Write a Python program to display the current date and time.')
from datetime import datetime
print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"));


print('\n\n')

# Program 4:
print('4) Write a Python program which accepts the radius of a circle from the user and compute the area.')
from math import pi
radius = float(input ("Radius of the circle : "))
print('Area of Circle is:' + str(pi * radius**2));


print('\n\n')


# Program 5: 
# Note: I'm using raw_imput because my python version is 2.7.15. input() is not acceptable.
print('5) Write a Python program which accepts the user\'s first and last name and print them in reverse order with a space between them.')
fName = raw_input('Enter FirstName:')
lName = raw_input('Enter LastName:')
print('Your name in Reverse Order is: '+ lName + ' '+ fName)


print('\n\n')


# Program 6:
print('6) Write a python program which takes two inputs from user and print them addition')
num1 = input('Enter Number One:')
num2 = input('Enter Number Two:')
addition = num1 + num2
print('Addition is: ' + str(addition))





