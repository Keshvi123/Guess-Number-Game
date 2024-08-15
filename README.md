<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Number Guessing Game</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            color: #333;
        }
        h1, h2 {
            color: #0056b3;
        }
        code {
            background-color: #f4f4f4;
            padding: 2px 4px;
            border-radius: 4px;
        }
        pre {
            background-color: #f4f4f4;
            padding: 10px;
            border-radius: 4px;
            overflow-x: auto;
        }
    </style>
</head>
<body>

    <h1>Number Guessing Game</h1>

    <p>Welcome to the Number Guessing Game! This Python application is a fun and interactive way to test your guessing skills. The game challenges you to guess a randomly generated number between 1 and 1000. The application provides hints to guide you and keeps track of all your guesses until you find the correct number.</p>

    <h2>Features</h2>
    <ul>
        <li>Generates a random number between 1 and 1000.</li>
        <li>Provides feedback on whether your guess is too high or too low.</li>
        <li>Keeps a record of all guesses made during the game.</li>
        <li>Notifies you when you've guessed the correct number.</li>
    </ul>

    <h2>Installation</h2>
    <p>To get started, you need Python installed on your computer. You can download Python from <a href="https://www.python.org/downloads/" target="_blank">python.org</a>.</p>

    <h3>Clone the Repository</h3>
    <pre><code>git clone https://github.com/yourusername/number-guessing-game.git</code></pre>

    <h3>Navigate to the Project Directory</h3>
    <pre><code>cd number-guessing-game</code></pre>

    <h2>Usage</h2>
    <ol>
        <li>Open a terminal or command prompt.</li>
        <li>Navigate to the project directory.</li>
        <li>Run the script with Python:</li>
    </ol>
    <pre><code>python guessing_game.py</code></pre>
    <p>4. Follow the prompts to enter your guesses. The game will provide feedback on each guess.</p>

    <h2>How It Works</h2>
    <ol>
        <li><strong>Importing Libraries:</strong> The <code>random</code> library is imported to enable the generation of a random number.</li>
        <li><strong>Generating a Random Number:</strong> <code>num = random.randint(1, 1000)</code> generates a random number between 1 and 1000.</li>
        <li><strong>Setting Up the Game Loop:</strong> Initializes variables and sets up a loop to keep prompting the user for guesses until the correct number is guessed.</li>
        <li><strong>User Input and Feedback:</strong> Prompts the user to guess, provides feedback, and records guesses.</li>
        <li><strong>Displaying All Guesses:</strong> Once the correct number is guessed, the list of all guesses is displayed.</li>
    </ol>
    <h2>Example</h2>
    <pre><code>Guess number from 1 to 1000: 500
Your guess is too high. Try a lower number!

Guess number from 1 to 1000: 250
Your guess is too low. Try a higher number!

Guess number from 1 to 1000: 375
Your guess is too high. Try a lower number!

Guess number from 1 to 1000: 312
Congratulations! You've guessed the correct number: 312

List of your guesses: [500, 250, 375, 312]
</code></pre>

<h2>Contributing</h2>
<p>We welcome contributions to enhance the game. If you have any suggestions or improvements, feel free to fork the repository and submit a pull request.</p>

<h2>License</h2>
<p>This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for details.</p>

<h2>Contact</h2>
<p>For any questions or further information, please contact <a href="mailto:your.email@example.com">Your Name</a>.</p>

</body>
</html>
