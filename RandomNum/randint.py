import random

jackpot=random.randint(1,100)

guess = int(input('Guess the number '))

while jackpot != guess:
    if(guess<jackpot):
        print('Guess higher ')
    else:
        print('Guess Lower ')
        
    guess = int(input('Guess the number '))
print('Jackpot right answer')