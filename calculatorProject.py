'''
Creating a calculator to add, subtract, divide or multiply any two numbers
that the user input and return the results to the user instantly;

@Created by Nchopereu Nelson on the 1 of September 2023, Accra Ghana.
'''
print('')
print("Welcome to our Impactnelson's Calculator! Here to make your life with numbers easier! 😉😉 ")
print('')
print("What are we doing today, my friend ?'")
print('😍😍😍😍😍😍😍😍😍')
print('')
print("Let's Calculate. 😉😉")
print('')

#Inputs 
num1= input('Enter the FIRST number: ')
print('')
operators = input('Enter the OPERATOR (/, x, +, -, or square): ')
print('')
num2 = input('Enter the SECOND number: ')
print('')
#Results conditions
if operators == '+':
    result = int(num1) + int(num2)
    print('Total: ', result)
elif operators == '-':
    result = int(num1) - int(num2)
    print('Total: ', result)
elif operators == 'x':
    result = int(num1) * int(num2)
    print('Total: ', result)
elif operators == '/':
    result = int(num1) / int(num2)
    print('Total: ', result)
elif operators == 'square':
    result = int(num1) ** int(num2)
    print('Total: ', result)
else:
    print('You Entered An Invalid Operator')

print('')
print("Thank you for using Impactnelson's Calculator!")