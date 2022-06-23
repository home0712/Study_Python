############ Basic Calculator ############

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result1 = num1 + num2 # just gonna make this as a string in python
result2 = int(num1) + int(num2) # convert both number into whole numbers
result3 = float(num1) + float(num2) # convert a number into decimal numbers

print(result1) # string
print(result2) # error if num1 or num2 is decimal numbers
print(result3) 

