#Python Quize Game by Nchopereu Nelson @Sept 6, 2023, Ghana.

name = input('\nWhat is your name please?\n')
print(f'\nWelcome to this Impact Python Quize Game, {name}\nLet us proceed!\n All the best in your answers!')


questions = ("How many elements are in the periodic table?\n",
             "Which animal lays the largest eggs?\n",
             "What is the longest river in Africa?\n",
             "What is the largest economy in Africa?\n",
             "What is the largest economy in the wolrd?\n",
             "Who was the first black president of South Africa?\n",
             "What does humans take in for a living?\n",
             "What do humans emit into the air as waste?\n",
             "What does plant emit as waste that is so useful to humans?\n",
             "What shape is the earth?\n")

options = (("A. 118", "B. 75", "C. 360", "D. 108"),
           ("A. Penguin", "B. Dog", "C. Ostrich", "D. Python"),
           ("A. Nile River", "B. Niger River", "C. Congo River", "D. Nile"),
           ("A. Zimbabwe", "B. Ghana", "C. Nigeria", "D. South Africa"),
           ("A. Russia", "B. United States", "C. China", "D. Russia"),
           ("A. Nelson Mandela", "B. Jacob Zuma", "C. Ramaphosa", "D. Paul Biya"),
           ("A. Rocks", "B. Water", "C. Food", "D. Love"),
           ("A. Fresh Air", "B. Oxygen (O2)", "C. Carbon dioxide (CO2)", "D. Nitrogen"),
           ("A. Carbon dioxide", "B. water vapor", "C. Oxygen", "D. bad smell"),
           ("A. Spherical", "B. Circular", "C. Round", "D. U-shapped"))

answers = ('A','C','A','D','B','A','C','C','C','A')


guesses = []

score = 0

question_number = 0


for question in questions:
    print("__________________________________")
    print(question)
    for option in options[question_number]:
        print(option)
        
        
    guess = input('Enter A, B, C, or D: ').upper()
    guesses.append(guess)
    if guess == answers[question_number]:
        print('✅CORRECT!')
        score += 1
    else:
        print('❌INCORRECT!')
        print(f'{answers[question_number]} is the correct answer!')
        
        
    question_number += 1
    
print('\n--------------------------------\n')
print('\n----------RESULTS---------------')
print("--------------------------------\n")

print("\n ANSWERS")
print("--------------------------------\n")
print("\nThe correct Answers are:✅✅ ", answers, end="\n")
print("\nYour Answers were:      👉👉 ", guesses, end="\n")
print("--------------------------------\n")

score = int(score / len(questions) * 100)

print(f'\n{name}, Your score is {score}% over 100\n\n')

    
if score == 50:
    print('Congratulations👌, you scored above average!\n')
# elif score  50:
#     print('You almost failed the test, try better next time\n')
elif score < 50:
    print('You scored below Average.😔😔 Unseccessful!! Try harder next time!\n')
elif score >= 80:
    print("\nCONGRATULTIONS!!😲😇 You did fantastically well.")
print (f'\nThank you for takeing the Quiz.\n\nGoodbye, {name}!😉\n')
