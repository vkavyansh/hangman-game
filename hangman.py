print("Let's begin the game!\nGuess the correct word")

# for choosing random words
import random
word_list = ["black","codeaplha","apple","dog","donut","python","engineer"]
lives = 6
chosen_word = random.choice(word_list)

# stages of hangman
stages = [
    """
    +---+
    |   |
        |
        |
        |
       ===
    """,
    """
    +---+
    |   |
    O   |
        |
        |
       ===
    """,
    """
    +---+
    |   |
    O   |
    |   |
        |
       ===
    """,
    """
    +---+
    |   |
    O   |
   /|   |
        |
       ===
    """,
    """
    +---+
    |   |
    O   |
   /|\\  |
        |
       ===
    """,
    """
    +---+
    |   |
    O   |
   /|\\  |
   /    |
       ===
    """,
    """
    +---+
    |   |
    O   |
   /|\\  |
   / \\  |
       ===
    """
]

# for displaying the blanks for that random word
display = []
for i in range(len(chosen_word)):
    display += '_'
print(display)

game_over = False


# main code of the game
while not game_over:
    guess = input("\n\nGuess a letter :").lower()
    for pos in range(len(chosen_word)):
        letter = chosen_word[pos]
        if letter == guess:
            display[pos] = guess
            print("\n\nlives left : ",lives)
    print(display)         

    if guess not in chosen_word:
        lives = lives - 1
        print("\n\nlives left : ",lives)
        if lives == 1:
            print("\n\nHANGMAN : Please save me :(")
        elif lives == 0:
            game_over = True
            print("\nCorrect word  :", chosen_word)
            print("\nGAME OVER\nDEAD!!")      
    if '_' not in display:
        game_over = True
        print("\nYou guessed the correct word :", chosen_word)
        print("\nYOU WIN!!")
        print("\nHANGMAN : You saved my life :)")

    print(stages[6 - lives]) # printing hangman stages as per the lives     

    

               
