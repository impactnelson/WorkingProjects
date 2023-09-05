#This program prints a fibonacci from of 10,000 from 0.
# A fibonacci sequence where each number is the sum of two preceeding numbers

def fibon(n):
    result = []
    a = 0 
    b = 1
    while a < n:
        a, b = b, a + b
        result.append(a)
    print('\n\nThe length this list is: ', len(result), end="\n\n")
    
    return result

print(fibon(10000))
print("\n\nHere ends the fibonacci of 0-10,000!\n\n")