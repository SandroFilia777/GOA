#დაველება 1
for i in range(6, 56, 5):
    print(i-1)

#დაველება 2
for i in range(2, 21, 2):
    print(i)

#დაველება 3
sum=1
for i in range(5, 11):
    sum *=i
print(f"sum of numbers from 5 to 10 is {sum}")

#დაველება 4
user_input=int(input("enter number: "))
factorial=1
for i in range (1,user_input+1):
    factorial*=i
print (f"factorial for {user_input} is {factorial} or {user_input}! is {factorial}")

#დაველება 5
user_input = int(input("Enter whole number: "))
if user_input % 2 == 0:
    user_input /= 2
    print(int(user_input))
else:
    new_num = user_input * 3 + 1
    print(new_num)
    
#დაველება 6
num=10
while num>=1:
    print(num)
    num-=1

#დაველება7
name=(input("Please enter your name: "))
while name!="quit":
    name=(input("Please enter your name: "))

#დაველება 8
num=10
while  num<20:
    print(num)
    num+=2

#დაველება 9
num =int(input("Please enter number: "))
while num<=0:
    num =int(input("Please enter number: "))

#დაველება 10
num=1
while num<=10:
    new_num=num**2
    print(new_num)
    num+=1
    