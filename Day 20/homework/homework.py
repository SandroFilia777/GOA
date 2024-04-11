#1
# def is_palindrome(word): 
#     return word == word[::-1]
# word = input("შეიყვანეთ სახელი: ")
# if is_palindrome(word):
#     print(f"{word} არის პალინდრომი.")
# else:
#     print(f"{word} არ არის პალინდრომი.")


#2




#3
def add_first_letter(words):
    new_word = ""
    for word in words:
        new_word += word[0]
    return new_word

words = input("შეიყვანეთ ხუთი სიტყვა: ").split()
result = add_first_letter(words)
print(result)



#4

first = list(range(10, 21))
second = list(range(30, 51, 5))
combined = first + second
print(combined)