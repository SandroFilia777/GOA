#1
def check_word():
    word = input("შემოიტანეთ სიტყვა: ")
    if len(word) >3:
        print(word[:3])
    else:
        print(word[0])

check_word()

#2
sliced_numbers = []
for i in range(10, 21, 2):
    sliced_numbers.append(i)

print(sliced_numbers)


#3
def get_word():
    word = input("შემოიტანეთ სიტყვა: ")
    return word
def reverse_word(word):
    return word[::-1]
user_word = get_word()
reversed_word = reverse_word(user_word)
print("შებრუნებულად სიტყვა:", reversed_word)
