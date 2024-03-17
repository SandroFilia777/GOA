#1
budget = int(input("What is your budget: "))
cost = int(input("Please enter cost: "))

if budget >= cost:
    print("You have enough money")
else:
    print("You dont have enough money")

#2
registered_password = "Messi is the best"

password = input("Please enter your password: ")

while password != registered_password:
    password = input("Please enter your password again: ")
    if password == registered_password:
        print("You have accses on your account")
    else:
        print("You have entered wrong password, please try again")

#3
start = int(input("Please enter starting value: "))
end = int(input("Please enter ending value: "))
step = int(input("Please enter step value: "))

for i in range(start,end,step):
  print(i)

#4
s1 = int(input("Please enter first side: "))
s2 = int(input("Please enter second side: "))
s3 = int(input("Please enter third side: "))


is_valid = (s1 + s2 > s3) and (s2 + s3 > s1) and (s3 + s1 > s2)

while is_valid != True:
    s1 = int(input("Please enter first side: "))
    s2 = int(input("Please enter second side: "))
    s3 = int(input("Please enter third side: "))

    is_valid = s1 + s2 > s3


#5
min_value = int(input("შეიყვანეთ მინიმალური მნიშვნელობა: "))
max_value = int(input("შეიყვანეთ მაქსიმალური მნიშვნელობა: "))

for num in range(min_value, max_value + 1):
  if num > 1:
    sum = True
  for i in range(2, num):
    if (num % i) == 0:
      sum = False
      break

#6
operation = input("Please enter operation (+,-,*,/): ")
num1 = int(input("Please enter first number: "))
num2 = int(input("Please enter second number: "))

if operation == '+':
    print(num1 + num2)
elif operation == '-':
    print(num1 - num2)
elif operation == '*':
    print(num1 * num2)
elif operation == '/':
    print(num1 / num2)
else:
    print("operation is not valid")

#7