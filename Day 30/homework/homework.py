# დავალება 1
def reverse_and_uppercase(input_string):
    reversed_uppercase_string = input_string[::-1].upper()
    return reversed_uppercase_string

input_str = "goal oriented academy"
result = reverse_and_uppercase(input_str)
print(result) 
# დავალება 2
def categorize_and_uppercase(strings):
    odd = []
    even = []

    for s in strings:
        if len(s) % 2 == 0:
            even.append(s.upper())
        else:
            odd.append(s.upper())

    print("Odd:", odd)
    print("Even:", even)

strings_list = ["vano", "nika", "bubazi", "zauri"]
categorize_and_uppercase(strings_list)
# დავალება 3
def process_strings(strings):
    result = []

    for s in strings:
        if len(s) % 2 == 0:
            result.append(s.upper())
        else:
            result.append(s[0].upper() + s[1:].lower())

    print(result)

test_case = ["goa_best", "vano", "nesvi", "tskhVarAdzE"]
process_strings(test_case)
# დავალება 4
def process_mixed_case_strings(strings):
    result_list = []

    for s in strings:
        if s.isupper():
            result_list.append(s.lower())
        elif s.islower():
            result_list.append(s.upper())
        else:
            result_list.append(s)

    print(result_list)

test_case = ["vano", "DAVIT", "LUKA", "nika"]
process_mixed_case_strings(test_case)
# დავალება 5
def process_string_based_on_find(input_string, char_to_find):
    index = input_string.find(char_to_find)
    
    if index == -1:
        return "Character not found in the string."
    
    if index % 2 == 0:
        return input_string.upper()
    else:
        return input_string.capitalize()

test_case = "vano motiashvili"
char_to_find = "n"
result = process_string_based_on_find(test_case, char_to_find)
print(result)

char_to_find = "m"
result = process_string_based_on_find(test_case, char_to_find)
print(result)