name = input("What is your name?")
print(f"Hello, {name}. Time to play Hangman!!")

word = "secret"
guesses = ''
tries = 3

while tries > 0:
    blanks = 0

    for char in word:
        if char in guesses:
            print(char, end="")
        else:
            print("_", end=" ")
            blanks += 1
    
    if blanks == 0:
        print("\nYou got it. You won!!")
        break

    guess = input("\nGuess a character: ")
    guesses += guess

    if guess not in word:
        tries -= 1
        print(f"Sorry, that was wrong... {tries} guesses remaining")
        if tries == 0:
            print("You lost!!")
            break