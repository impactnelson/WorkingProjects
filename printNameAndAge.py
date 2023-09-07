"""
- Ask for name, of the customer,
- print how long the name is,
- And ask for age,
- Then print how old he is todayand how old he or she will be in 2025.
"""
print('This my first program with Automate the boring stuff book')
print('')
print('')

print('Hello, there')
print('')
print('What is your name?') #Ask for their names.
print('')
myName = input('')
print('')
print('It is a pleasure to meet you {}'.format(myName))
print('')
#length = (len(myName))
#print('The length of your name is: ', length)
print(myName,', Could you tell us your age?') #Ask for their age
myAge = input('')
#addNum = 2
print('You are {} years Old today!'.format(myAge))
print('')

my2025 = int(myAge) + 2

print('You will be {} years old by 2025!'.format(my2025))
