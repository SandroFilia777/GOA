#შექმენით სტრინგი სადაც გექნებათ 6 სიმბოლო, ხოლო ჩამოაჭერით ამ სტრინგს მისი მეორე ნახევარი
# 2) შექმენით სია სადაც slice ინგის გამოყენებით ჩამოაჭრით პირველ 4 ელემენტს
# 3) ბონუსი: შექმენით 8 ელემენტიანი სია, და slice ინგის გამოყენებით გამოიტანეთ მხოლოდ ლუწ ინდექსებზე მდგომი რიცხვები
# მინიშნვბა: როგორც range() მუშაობს ისე იმუშავებს slice ინგიც

# #1
# list=["sandro"]
# print(list[0:3])

# #2
# list2=["pepsi","coca-cola","sprite","fanta","phone","drinks"]
# print(list2[4:6])


# #3
# list = [1,2,3,4,5,6,7,8]
# list2 = []
# for i in range(len(list)):
#      x = slice(i-1, i+1)
#      if i%2 == 0:
#           list3 = list[x]
#           list2.append(list3[0])
# print(list2)

# #4
# numbers = []

# start = 0
# end = 5 + 1
# step = 1

# while start < end:
#     numbers.append(start)
#     start = start + step

# print(numbers)

# #5
# names = ["Luka", "Lile", "Nia", "Mate", "Ruti"]

# sliced_list = []

# start = 0
# end = 5
# step = 2

# while start < end:
#     sliced_list.append(names[2])
#     start = start + step

# print(sliced_list)

#6
 
numbers= []

start = 27
end = 0 
step = -1
while start > end:
    numbers.append(start)
    start=start+step
print(numbers)

#7


