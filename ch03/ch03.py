############### Dictionaries ###############

# Convert 3 digits month name into the full month name

monthConversions = {
	# key: value
	# keys are unique (not allowed duplicate)
	
	0: "January",
	1: "February",
	10: "March",
	"Jan": "January",
	"Feb": "February",
	"Mar": "March",
	"Apr": "April",
}


print(monthConversions["Mar"])
print(monthConversions.get("Jan"))
print(monthConversions.get("Luv")) # None
print(monthConversions.get("Luv", "Not a valid Key")) # give us a defalut value



############### While Loop ###############

i = 1

while i <= 10: # continue this loop as long as the condition is true
	print(i)
	i += 1 # i = i + 1
	
print("Done with loop")


	
