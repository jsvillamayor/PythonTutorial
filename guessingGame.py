import random
print("You have 3 guesses to guess my secret number!")
secret = random.randrange(10)
guessNum = 0
guessLimit = 3
while guessNum < guessLimit:
    guess = int(input("Guess: "))
    guessNum += 1
    if guess == secret:
        print("You win!")
        break
    else:
        if guessNum == 3:
            print('You lose!')
