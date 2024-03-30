firstname = input("Please enter your firstname: ")
lastname = input("Please enter your lastname: ")

person_info = [firstname, lastname]

print(person_info)

numbers = [10,11,12,13,14,15,16,17,18,19,20]

numbers[0] = 1
numbers[2] = 1
numbers[4] = 1
numbers[6] = 1
numbers[8] = 1
numbers[10] = 1

print(numbers)

numbers = [1,2,3,4,5,6,7,8,9,10]

size = len(numbers)
last_index = size - 1

print(numbers[0])
print(numbers[last_index])

#1)
firstname = "Giorgi"

for i in range(0, len(firstname)):
    print(firstname[i])

#2)
firstname = "Giorgi"

for i in range(0, len(firstname), 2):
    print(firstname[i])


numbers = [1,2,3,4,5,6,7,8,9,10]

if 5 in numbers:
    print("Yes 5 is in numbers list")
else:
    print("No 5 is not in numbers list")


numbers = [1,2,3,4,5,6,7,8,9,10]

result = 0

for num in numbers:
    if num % 2 == 0:
        result = result + num

print(result)