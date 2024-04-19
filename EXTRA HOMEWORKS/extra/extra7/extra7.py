#The Simplest Math Problem No One Can Solve
# Collatz Conjecture
def collatz(x):
    sequence = [x]
    while x > 1:
        if x % 2 == 0:
            x = x // 2
        else:
            x = 3 * x + 1
        sequence.append(x)
    return sequence
start_number = int(input("Enter a starting number: "))  
result_sequence = collatz(start_number)
print("Collatz sequence for", start_number, ":", result_sequence)


