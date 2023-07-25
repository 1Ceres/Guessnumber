import random
print("Welcome to Guess number game.")
print("I'm thinking about number between 1 and 100.")
diff = input("Choose a difficulty. Type 'easy' or 'hard': ")
if diff == 'easy':
    level = 10
elif diff == 'hard':
    level = 5
number = random.randint(1,100)
while level > 0:
    print(f"You have {level} attemps remaining to guess a number.")
    guess = int(input("Make a guess: "))
    if guess == number:
        print(f"You won, the number is indeed: {guess}")
        break
    elif guess > number:
        print("Too high")
    elif guess < number:
        print("Too low.")
    level -= 1
if level == 0:
    print(f"You ran out of guesses, the number was: {number}")