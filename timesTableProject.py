'''
This program generates a multiplication table from 1 to 10 using nested loops. 
It calculates and prints the product of all combinations of numbers from 1 to 10
'''
print('The Multiplication of All Numbers from 1 - 20')
print("")
for num in range(1, 21):
    for i in range(1, 21):
        j = num * i
        print('%s X %s: %s!' % (num, i, j))
        # if num == 11: break
        print('')
    # if num == 10: break
    print('')
    print('')
print('Multiplication Done')
print('')