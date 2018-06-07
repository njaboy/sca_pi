import random
i = 0
random_number = random.randint(1,10)
while i < 10:
    i = i + 1
    guess = int(raw_input("Guess a number from 1 to 10: "))
    if guess < random_number:
        print 'Guess is to low'
    else:
        if guess > random_number:
            print 'Guess is too high'
        else:
            print 'You Guessed it'
            break
