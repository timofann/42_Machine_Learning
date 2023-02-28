from random import randint

welcome = """\
This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!
"""

if __name__ == '__main__':
    print(welcome)
    attempts = 0
    n = randint(1, 99)
    answer = 'start'
    while answer != 'exit':
        answer = input("What's your guess between 1 and 99?\n")
        attempts += 1
        try:
            if int(answer) == n:
                print("Congratulations, you've got it!")
                print(f"You won in {attempts} attempts!")
                break
            elif int(answer) > n:
                print("Too high!")
            else:
                print("Too low!")
        except:
            print("That's not a number.")
    if answer == 'exit':
        print('Goodbye!')






