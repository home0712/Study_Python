########### Better Calculator ###########

# get input from the users
num1 = float(input("Enter 1st number: ")) # directly convert input into a number
op = float(input("Enter operator: "))
num2 = float(input("Enter 2nd number: "))

if op == "+":
	print(num1 + num2)
elif op == "-":
	print(num1 - num2)
elif op == "/":
	print(num1 / num2)
elif op == "*":
	print(num1 * num2)
else:
	print("Invalid operator")
	
