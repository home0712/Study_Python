########## Build a Translator ##########
# 
word = "something"
vowels = [a, e, i, o ,u]

def translate(word):
  translation = ""
  for letter in word:
    if letter in "AEIOUaeiou":
      translation += "g"
    else:
      translation += letter
  return translation

print(translation(input("Enter a phrase")))



  
