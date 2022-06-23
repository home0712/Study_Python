############ String ############



############ Numbers ############

my_num = 5

# string concatenation
print(str(my_num) + "my favorite number")
print(my_num + "my favorite number") # string concatenation 불가

# absolute number
print(abs(my_num))

# power
print(pow(3, 2)) # 3^2 = 9

# minimum
print(min(4, 6))

# maximum
print(max(4, 6))

# round (반올림)
print(round(3.2))
print(round(3.7))

# import external stuff (module) on the top of the file
# to use math functions
from math import * 

print(floor(3.2))
print(cell(3.7))
print(sqrt(36)) # square root



############ Getting Input From Users ############

name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "! You are " + age)








