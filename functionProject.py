'''
README.md
Here's a quick summary of how it works:

The greetings function is called initially to greet the user with their name and age.
The while True loop inside the greetings function continues to prompt for names and ages until the user enters 'exit' or 'quit'.
When 'exit' or 'quit' is entered, the loop breaks, and the function returns.
After the function call, a thank you message is printed.
'''
def greetings(name, age):
    print(f'Hello {name}, you are {age} years old!\n')
    while True:
        name1 = input("Enter another name (OR, type 'exit' or 'quit' to stop!)\n")
        if name1 == 'exit':
            break
        elif name1 == 'quit':
            break
        age1 = input('\nEnter age:\n')
        if age1== exit:
            break
        print(f'Hello {name1}, you are {age1} years old\n')
name = input("\nWhat is your name? \n")
age = input("\nHow Old are you?\n")
age = int(age)
print(greetings(name, age))
print('\nThank you for your time with us!\n\n')

'''@All Rights Reserved: @Author: impactnelson-Nchopereu Nelson'''