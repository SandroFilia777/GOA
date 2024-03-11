#დავალება 1
# 1-დან 50-ის ჩათვლის 5-ის ჯერადები
for i in range(6, 56, 5):
    print(i-1)

#დავალება 2
# 2-დან 20-ის ლუწი რიცხვები
for i in range(2, 21, 2):
    print(i)

#დავალება 3
# 5-იდან ათის ჩათვლით რიცხვების ნამრავლი
    
for i in range(5, 11):
    pasuxi = i * i
    print(f"{i} * {i} = {pasuxi}")

# #დავალება 4
print(input("enter number"))
def fact( n):
  if n>1:
    return n*fact(n-1)
  else:
    return 1.
n=int(input('enter the number'))
print("Factorial of ",n,"is - ", fact(n))


 #დავალება 5
    
    

    
#დავალება 6
#დაიწყეთ 10-დან და დაითვალეთ 1-მდე, დაბეჭდეთ თითოეული რიცხვი.

for i in range(10, 1, -1):
     print(i)

#დავალება 7
name=str(input("Please enter your name: "))
if name =="quit":
   print("you are in")
elif name!="quit":
   print("its incorrect")

#დავალება 8
for i in range(10,21,2):
   print(i)

#დავალება 9
num =int(input("Please enter positive number: "))
if num >0:
   print("you have written positive number.")
elif num <0:
    (print("you have written negative number."))

#დავალება 10
for i in range(1, 11):
    print(i*i)
