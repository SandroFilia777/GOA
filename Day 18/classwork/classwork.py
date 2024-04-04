names = ["Nika", "Luka", "Gabrieli", "Dato", "Mate"]

for i in names:
    print(i)


numbers = [1,2,3,4,5,6,7,8,9,10]

for number in numbers:
    if number % 2 == 0:
        print(number)

numbers = [1,2,3,4,5,6,7,8,9,10]

sum = 0
multiple = 1

for num in numbers:
    sum = sum + num
    multiple = multiple * num

print(numbers,"sum of these numbers is",sum)
print(numbers, "multiple of these numbers is", multiple)

name = "Luka"

for char in name:
    print(char)


    