
#example
name = "Giorgi"
even_indexes_string = ''
        #  0 1 2 3 4 5
for i in range(0, len(name)):
    if i % 2 == 0:
        even_indexes_string = even_indexes_string + name[i]

print(even_indexes_string)



name = "dato"
even_indexes_string = ''
        #  0 1 2 3 4
for i in range(0, len(name)):
    if i % 2 == 0:
        even_indexes_string = even_indexes_string + name[i]

print(even_indexes_string)


name = "dato"
even_indexes_string = ''
        #  0 1 2 3 4 5 6
for i in range(0, len(name)):
    if i % 2 == 0:
        even_indexes_string = even_indexes_string + name[i]

print(even_indexes_string)



name = "lika"
even_indexes_string = ''
        #  0 1 2 3 4 5 6 7 
for i in range(0, len(name)):
    if i % 2 == 0:
        even_indexes_string = even_indexes_string + name[i]

print(even_indexes_string)



name = "sandro"
even_indexes_string = ''
        #  0 1 2 3 4 
for i in range(0, len(name)):
    if i % 2 == 0:
        even_indexes_string = even_indexes_string + name[i]

print(even_indexes_string)




num = 5
# num = num - 1
num -= 1

# num = num + 6
num += 6

# num = num / 2
num /= 2

# num = num * 2
num *= 2
# num = num % 6
num %= 2

print(num)