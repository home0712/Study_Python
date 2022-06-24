########### List ###########

# any types can be listed in a list in python
# numbers, strings, or booleans...

friends = ["Kevin", "Karen", "Jim"] # OK
friends_mix = ["Kevin", 2, False] # OK

# how can we access the values inside of a list?
print(friends) # ['Kevin', 'Karen', 'Jim']

# to access a specific element
i = 0
print(friends[i]) # i is an index

print(friends[-1]) # to access the back of the list; it starts indexing from the back of the list

print(friends[1:]) # start indexing from 1 to the end

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
print(friends[1:3])

# modify a list
friends[1] = "Mike"



########### List Functions ###########
lucky_numbers = [4, 8, 15, 16 ,23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

# extend(list): add another list after a list
friends.extend(lucky_numbers)

# append(value): add an individual number onto the end of a list
friends.append("Creed")

# insert(index, value): add a number into the middle of the list
friends.insert(1, "Kelly")

# remove(value): remove a value from the list
friends.remove("Jim")

# clear(): remove all of the elements from the list
friends.clear()

# pop(): get rid of the last element inside the list 
friends.pop()

# index(value): get an index of a value
friends.index("Kevin")
friends.index("Mike") # error if a value is not in the list

# count(value): count how many times a value shows up
friends.count("Jim")

# sort(): sort a list basically in (alphabetical) order
friends.sort()

# reverse(): reverse the order of a list
friends.reverse()

# copy(): copy a list
friends2 = friends.copy()




########### Tuples ###########
## difference between tuples vs. list

# tuples = immutable containers (can't be changed or modified)

coordinates = (4, 5) 
# coordinates[1] = 10 : error! (tuple is immutable)
print(coordinates[1])

# a list of tuples
coordinates2 = [(4, 5), (6, 7), (80, 90)] # tuples' never gonna be changed




########### Functions in Python ###########

def say_hi(): 
  # automatically indented (inside a function)
  print("Hello User")
  

# call a function & flow of a function
print("Top")
say_hi()
print("Bottom")

# a function with parameters
def say_hi2(name, age):
  print("Hello " + name + " you are " + str(age))
  
say_hi2("Mike", 35)
say_hi2("Steve", 70)




########### Return Statement ###########

def cube(num):
  return num*num*num
  print("code") # isn't gonna work
  
# print(cube(3))  OK

result = cube(4)
print(result)




########### If Statement ###########

is_male = True
is_tall = True

if is_male: # if (is_male == true)
  print("You are a male")
else:
  print("You are not a male")


if is_male or is_tall:
  print("You are a male or tall or both")
else:
  print("You are neither male nor tall")


if is_male and is_tall:
  print("You are a tall male")
elif is_male and not(is_tall):
  print("You are a short male")
elif not(is_male) and is_tall:
  print("You are not a male but are tall")
else:
  print("You are not a male and not tall")




########### If Statements & Comparisons ###########

def max_num(num1, num2, num3):
  if num1 >= num2 and num1 >= num3:
    return num1
  elif num2 >= num1 and num2 >= num3:
    return num2
  else:
    return num3
  
print(max_num(3, 4, 5))

# comparison operators
num1 == num2
num1 != num2








