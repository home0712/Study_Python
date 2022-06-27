## uppercase <-> lowercase
#### functions ####
# string.isupper(): check if all characters in a string is uppercase
# string.islower()
# string.upper(): change the lowercases in the string into uppercase 
# string.lower()

def swap_case(s):
    new = ""
    for letter in s:
        if letter.isupper():
            new += letter.lower()
        elif letter.islower():
            new += letter.upper()
        else:
            new += letter
    return new
