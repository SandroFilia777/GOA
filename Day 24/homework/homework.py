#დავალება 1
x = 0
def num(num2):
    for i in num2:
        if i % 2 == 0:
            x +=1
            return x
        nums=[1,2,3,4,5,6,7,8,9,10]
        result = num(nums)
        print(result)
#დავალება 2

def square_area(length,width):
    return length * width
length = 5
width = 4
result = square_area(length,width)
print(result)