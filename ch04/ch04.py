########## For Loops ##########

friends = ["Jim", "Karen", "Kevin"]

for index in range(len(friends)):
  if index == 0:
    print("first Iteration")
  else:
    print("Not First")
    

    
########## Exponent Function ##########

# basic
print(2**3)

# function
def raise_to_power(base, power):
  result = 1
  for index in range(power):
    result *= base
  return result

raise_to_power(2, 3) # 2 ^3 = 8



########## 2D Lists & Nesteed Loops ##########

# basic 2D List (4 rows / 3 cols)
number_grid = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9],
	[0]
]

print(number_grid[index_of_rows][index_of_cols])
print(number_grid[0][2])

# print each row: number_grid[row][]
for row in number_grid:
	print(row)

# print each values: number_grid[row][col]
for row in number_grid:
	for col in row:
		print(col)
		


########## Comments ##########

# comments a line

'''
hi python
comments mutiple lines
'''



########## Try / Except ##########

try:
	value = 10 / 0 # error type1 occurs
	number = int(input("Enter a number")) # error2 occurs
	print(number)
except ZeroDivisionError as err: # catching specific error
	print(err) # print out what went wrong
except:
	print("Invalid Input")
	

	
########## Reading Files ##########

# reading from external files (.txt, .html ...)

''' 
employees.txt
Jim - Salesman
Dwight - Salesman
Pam - Receptionist
Michael - Manager
Oscar - Accountant
'''

### app.py ###


employee_file = open("employees.txt", "r") # open the file and allows to read it
# "r" stands for "read" / 
# "a" = "append" the information at the end of the file
# "r+" = "read and write"

# check if a file is readable
print(employee_file.readable())

# spit out all the info of a file
print(employee_file.read())

# just read a line
print(emplyee_file.readline()) # 1st line
print(emplyee_file.readline()) # 2nd line ...

# take the all lines in the file and put them in an arrry
print(emplyee_file.readlines())
print(emplyee_file.readlines()[1]) # just read a line 

for employee in employee_file.readlines():
	print(emplyee)

# make sure to close the file after you read a file
employee_file.close()



########## Writing to Files ##########

# modify or append to a file

# appending
# !! if you execute more than once, it occurs an duplicate or problem
employee_file = open("employees.txt", "a") 
print(employee_file.write("\nToby - Human Resources"))
employee_file.close()

# overwrite a file or write (create) a entirely new file
employee_file = open("employees1.txt", "w") # create a new file
# employee_file = open("employees.txt", "w") # overwrite an existing file
# employee_file = open("index.html", "w")
print(employee_file.write("\nToby - Human Resources"))
employee_file.close()



########## Module & Pip ##########

# Module
# Documentation of list of python modules / 3rd party modules: python-docx
# where are they? they are stored in External Libraries -> Lib
# few things are built-in (not in the Lib)

### useful_tools.py ###
import random

feet_in_mile = 5280
meters_in_kilometer = 1000
beatles = ["John", "Paul", "Geroge", "Ringo"]

def get_file_ext(filename):
	return filename[filename.index(".") + 1:]

def roll_dice(num):
	return random.randint(1, num)

### app.py ###
import useful_tools

print(useful_tools.roll_dice(10)) # able to access all of the stuffs in the file


# Pip
# able to use pipe to install python modules 
# refers to as a package manager
# in the commnand window


########## Classes & Objects ##########

# to deal with real world data besides basic types of data
# to define my own data type

### Student.py ###
class Student:
	
	# map out what attributes a student should have
	def __init__(self, name, major, gpa, is_on_probation): # self is referring to the actual object
		self.name = name 
		self.major = major
		self.gpa = gpa
		self.is_on_probation = is_on_probation
		

### app.py ###
from Student import Student # from the Student file, I want to import the Student class

student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Pam", "Art", 2.5, True)

print(student1.name)
print(student1.gpa)
print(student2.gpa)

