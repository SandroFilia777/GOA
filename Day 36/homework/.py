def convert_to_initials(name):
    first_name, last_name = name.split()
    first_initial = first_name[0].upper()
    last_initial = last_name[0].upper()
    initials = f"{first_initial}.{last_initial}"
    return initials

# Test cases
print(convert_to_initials("vako natsvlishvili"))

#2
def sum_mix(arr):
    return sum(int(x) for x in arr)


print(sum_mix([9, 3, '7', '3']))

#3
def find_smallest_int(arr):
    return min(arr)

print(find_smallest_int([34, 15, 88, 2]))  # Output: 2
print(find_smallest_int([34, -345, -1, 100]))  # Output: -345