# Number Guessing Game

This Python program is a simple number guessing game where the user attempts to guess a randomly selected number between 1 and 1000. The program provides feedback on whether the guess is too high or too low and keeps track of all guesses. Upon guessing the correct number, it displays a list of all guesses made during the game.

## How to Play

1. The program will select a random number between 1 and 1000.
2. Enter your guess when prompted.
3. The program will inform you if your guess is too high or too low, and will continue to prompt for guesses until the correct number is guessed.
4. After guessing correctly, the program will display the list of all guesses made.

## How to Run

1. Make sure you have Python installed on your computer. You can download it from [python.org](https://www.python.org/).

2. Clone this repository or download the script file.

3. Open a terminal or command prompt.

4. Navigate to the directory containing the script file.

5. Run the script using the following command:
    ```bash
    python number_guessing_game.py
    ```

## Code

Here's the complete code for the number guessing game:

```python
import random

# Randomly select a number between 1 and 1000
num = random.randint(1, 1000)
guess = -1
guesses = []

# Loop until the correct number is guessed
while guess != num:
    # Prompt user for a guess
    guess = int(input("Guess a number from 1 to 1000: "))
    guesses.append(guess)
    
    # Provide feedback based on the guess
    if guess > num:
        print("Your Guess is too High, Lower number Please!!")
    elif guess < num:
        print("Your Guess is too Low, Higher number Please!!")
    else:
        print(f"Your Guess is Correct!! It was {guess}")

# Display the list of all guesses made
print("List of Your Guesses is: ", guesses)

