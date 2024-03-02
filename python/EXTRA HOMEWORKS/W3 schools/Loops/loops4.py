#Looping Through a String

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#The continue Statement
  
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
#Exit the loop when x is "banana", but this time the break comes before the print:
  
  fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
#The break Statement
  
  fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break