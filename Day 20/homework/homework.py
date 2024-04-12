# 1
def is_palindrome(word): 
    return word == word[::-1]
word = input("შეიყვანეთ სახელი: ")
if is_palindrome(word):
    print(f"{word} არის პალინდრომი.")
else:
    print(f"{word} არ არის პალინდრომი.")


# #2


# def find_duplicates():
#     person_input = int(input("Tell me how many times do you want to enter numbers: "))
#     list1 = []
#     for i in range(person_input):
#         new_num = int(input("Enter number: "))
#         list1.append(new_num)
#     list2 = []
#     for num in list1:
#         if list1.count(num) >= 2 and num not in list2:
#             list2.append(num)
#     if len(list2) == 0:
#         print("List is empty")
#     else:
#         print(list2)
# find_duplicates()


# 3
# def add_first_letter(words):
#     new_word = ""
#     for word in words:
#         new_word += word[0]
#     return new_word

# words = input("შეიყვანეთ ხუთი სიტყვა: ").split()
# result = add_first_letter(words)
# print(result)



# #4

# first = list(range(10, 21))
# second = list(range(30, 51, 5))
# combined = first + second
# print(combined)