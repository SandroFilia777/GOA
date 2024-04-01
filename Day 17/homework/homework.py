#1
list1 = [  "sandro","dato", "mate", "vako" , "giorgi"]
print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])
print(list1[4])
#2
list2 = [  "sandro","dato", "mate", "vako" , "giorgi"]

for name in list2:
    print(name)
#3
total = 0
product = 1

for number in range(1, 11):
    total += number
    product *= number

print(total)
print(product)
#4
total = 0

for number in range(2, 11, 2):
    print(number)
    total += number

print(total)
#5
total= 0
product = 1

for number in range(1, 11, 2):
    print(number)
    total += number
    product *= number

print( total)
print(product)
#6
wird = "goal oriented academy"

for e in wird:
    print(e)
#7
goa = "goal oriented academy"

for i in range(0, len(goa), 2):
    print(goa[i])