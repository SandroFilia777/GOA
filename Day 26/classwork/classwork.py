# def print_name(name, amount):
#     for i in range(amount):
#         print(name)


# print_name("luka", 5)

# print_name("Mate", 10)

# print_name("Saba", 2)



#1
# def smth(start, end):
#     for i in range(start,end):
#         print(i)
# smth(4,10)
# smth(2,23)
# smth(6,43)

#2
# def calculate_sum(start, end):
#     result = 0
#     for i in range(start, end):
#         result = result + i
#     print(result)

# calculate_sum(2,5)

#3
#def calculate_arithmetic(start, end):
#     numbers = []

#     for i in range(start, end):
#         numbers.append(i)
    
#     result = sum(numbers) / len(numbers)

#     print(result)

# calculate_arithmetic(5, 11)

#6
# def sum_of_two_numbers(a, b):
#     return a + b

# result = sum_of_two_numbers(3, 5)
# print("შედეგი:", result)
# #7

# def sum_of_list(numbers):
#     return sum(numbers)

# numbers = [1, 2, 3, 4, 5]
# result = sum_of_list(numbers)
# print("სიის რიცხვების ჯამია:", result)
# #8

def add_even_letters(name):
    result = " "
    for i, letter in enumerate(name):
        if i % 2 == 0:
            result += letter
    return result

name = "სანდრო"
result = add_even_letters(name)
print("ლუწ ინდექსიანი ასოები:", result)