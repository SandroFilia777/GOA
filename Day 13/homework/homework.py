# დავალება 1
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")   
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)

# დავალება 2
        
num = int(input("Please enter the number:"))
if num < 0 :
    print("This number is negative.")
elif num > 0 :
    print("This number is positive.")
else :
    print("This number is zero.")

# დავალება 3
    
for i in range(2, 101, 2):
    print(i)
# დავალება 4
total = 0
number = 1

while number <= 100:
    total += number
    number += 1

print("ყველა რიცხვის ჯამი 1-დან 100-მდე არის:", total)

# დავალება 5

day_number = int(input("Enter the day that you want from day 1 to day 7: "))

if day_number == 1:
    print("Monday")
elif day_number == 2:
    print("Tuesday")
elif day_number == 3:
    print("Wednesday")
elif day_number == 4:
    print("Thuresday")
elif day_number == 5:
    print("Friday")
elif day_number == 6:
    print("Saturday")
elif day_number == 7:
    print("Sunday")
else:
    print("The number doesn't match the numbers from the week.")
    
# დავალება 6
    
number = int(input("Please enter the number : "))

if number == 0:
    print("its zero")
elif number % 2 == 0:
    print("its even")
else:
    print("its even")