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
		




