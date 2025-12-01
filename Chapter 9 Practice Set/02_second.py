# The game() function in a program lets a user play a game and returns the 
# score as an integer. You need to read a file ‘Hi-score.txt’ which is either
# blank or contains the previous Hi-score. You need to write a program to 
# update the Hi-score whenever the game() function breaks the Hi-score.

import random

def game_highscore():
    print("Welcome to the game, enjoy you game...")
    score = random.randint(1,100)
    print(f"The number generated is{score}")

    with open("c:VS-Code_Python_Immature/VScode-Python/Chapter 9 Practice Set/highscore.txt") as f:
        highscores = f.read()
        if(highscores != ""):
            highscores = highscores
        else:
            highscores = 0

    print(f"Your score is:{score}")
    if(score > highscores):
        with open("c:VS-Code_Python_Immature/VScode-Python/Chapter 9 Practice Set/highscore.txt" , "w") as f:
            f.write(str(score))

        return score
    
game_highscore()






























