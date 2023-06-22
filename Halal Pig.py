# Name: Daniel Tran and Mathullah Teraei
# Date of Submission: June 22, 2023
# File Name: Halal Pig.py
# Desciption: HALAL PIG DICE is a game where you roll a dice and if that value is not 1, then you add it to your current score. You can choose to keep rolling, or
#           bank your points. If you roll a one at any point, your current score is lost and you lose your turn. If you bank your points, those points are permanent.
#           The first person to reach 100 or more points wins.

# Imports important modules, especially tKinter and the random module. It also imports time and os (which I'm not sure is used in the code)
from tkinter import *
import random, time, os

# Intializes all variables
#   - currentTurn determines who's turn it is
#   - score1 and 2 determines the players' permanent score
#   - current1 and 2 determine the player' concurrent score
#   - notClicked is used to pause the program until the player makes a decision
currentTurn = 1
score1 = 0
score2 = 0
current1 = 0
current2 = 0
notClicked = True

# Intializes the window
window = Tk()

# Sets the title
window.title("Halal Pig Dice Game")

# Sets the background color
window.configure(background = "black")

# The functions, they are:
#   - bankClickP1 and 2, they add their current score to their total and swap to the other person's turn
#   - keepRolling continues the current players turn by ending the while loop and rolling again
#   - diceRoll rolls the dice and returns the value
#   - quitGame quits the game if the button is pressed
def bankClickP1():
    global score1
    global notClicked
    global current1
    global currentTurn
    score1 += current1
    notClicked = False
    current1 = 0
    currentTurn = 2
def bankClickP2():
    global score2
    global notClicked
    global current2
    global currentTurn
    score2 += current2
    notClicked = False
    current2 = 0
    currentTurn = 1
def keepRolling():
    global notClicked
    notClicked = False
def diceRoll():
    roll = random.randint(1, 6)
    return roll
def quitGame():
    quit()
    
# Labels for the title, current turn, and player score. I could probably delete the last two but I'm scared I'm gonna break something.
Label (window, text="HALAL PIG DICE", bg="black", fg="white", font = "none 24 bold") .grid(row=1, column=5, sticky=W)
Label (window, text="Current turn:", bg="black", fg="white", font = "none 15 bold") .grid(row=3, column=5, sticky=W)
Label (window, text="Player " + str(currentTurn), bg="black", fg="white", font = "none 12 bold") .grid(row=4, column=5, sticky=W)

# Creates the quit button if the player wishes to exit the game
Button (window, text="Quit the Game", command=quitGame, bg="white", fg="black", font = "none 12 bold") .grid(row=8, column=5, sticky=W)

# The while loop for the entire game: it will loop until someone reaches the target score (being 100)
while score1 <= 100 and score2 <= 100:
    # Displays the total scores for both players
    Label (window, text="Player 1 Score: " + str(score1), bg="black", fg="white", font = "none 12 bold") .grid(row=4, column=5, sticky=W)
    Label (window, text="Player 2 Score: " + str(score2), bg="black", fg="white", font = "none 12 bold") .grid(row=4, column=6, sticky=W)
    
    # An if statement to check if whos' turn it is
    if currentTurn == 1:
        
        # Updates the current text accordingly
        Label (window, text="Current turn: Player 1", bg="black", fg="white", font = "none 15 bold") .grid(row=3, column=5, sticky=W)
        Label (window, text="Player " + str(currentTurn), bg="black", fg="white", font = "none 12 bold") .grid(row=4, column=5, sticky=W)
        
        # Runs the diceRoll function to determine the rolls
        play1 = diceRoll()
        
        # Tells the player what they rolled
        Label (window, text="You rolled a " + str(play1), bg="black", fg="white", font = "none 12 bold") .grid(row=5, column=5, sticky=W)

        # This if statement determines whether the roll was a 1 or not
        if play1 != 1:
            # This variable is set to true, so the program will not go forward until a decision is made
            notClicked = True

            # Adds the roll onto the player's current score
            current1 += play1

            # Gives two options for the player; bank the points or keep rolling
            Button (window, text="Bank the points", command=bankClickP1, bg="white", fg="black", font = "none 12 bold") .grid(row=7, column=5, sticky=W)
            Button (window, text="Keep rolling", command=keepRolling, bg="white", fg="black", font = "none 12 bold") .grid(row=7, column=6, sticky=W)

            # Until the player does something, the program will stop
            while notClicked:
                # Tells the player what their current score is
                Label (window, text="Your dice rolls are worth " + str(current1) + " would you like to bank the score or keep rolling?      \
                    ", bg="black", fg="white", font = "none 12 bold") .grid(row=6, column=5, sticky=W)
                
                # Updates the window so the window can actually open
                window.update()
                # Waits 0.1 seconds so the window doesn't update every frame, which causes lag
                time.sleep(0.1)

        # Otherwise, the roll is a ne    
        else:
            # Resets the player's current score
            current1 = 0

            # Briefly lets the player know they rolled a 1
            Label (window, text="You rolled a 1, get done out.                                                                            \
            ", bg="black", fg="white", font = "none 12 bold") .grid(row=6, column=5, sticky=W)

            # Goes to the other player's turn
            currentTurn = 2
            
    # This is the same as the code above, but adjusted for player 2
    else:
        Label (window, text="Current turn: Player 2", bg="black", fg="white", font = "none 15 bold") .grid(row=3, column=5, sticky=W)
        Label (window, text="Player 1", bg="black", fg="white", font = "none 12 bold") .grid(row=4, column=5, sticky=W)
        play2 = diceRoll()
        Label (window, text="You rolled a " + str(play2), bg="black", fg="white", font = "none 12 bold") .grid(row=5, column=5, sticky=W)
        if play2 != 1:
            notClicked = True
            current2 += play2
            Button (window, text="Bank the points", command=bankClickP2, bg="white", fg="black", font = "none 12 bold") .grid(row=7, column=5, sticky=W)
            Button (window, text="Keep rolling", command=keepRolling, bg="white", fg="black", font = "none 12 bold") .grid(row=7, column=6, sticky=W)
            while notClicked:
                Label (window, text="Your dice rolls are worth " + str(current2) + " would you like to bank the score or keep rolling?      \
                    ", bg="black", fg="white", font = "none 12 bold") .grid(row=6, column=5, sticky=W)
                window.update()
                time.sleep(0.1)
            
        else:
            current2 = 0
            Label (window, text="You rolled a 1, get done out.                                                                            \
            ", bg="black", fg="white", font = "none 12 bold") .grid(row=6, column=5, sticky=W)
            currentTurn = 1
            
        
    # Same reason as above
    window.update()
    time.sleep(0.1)

# Displays who won the game
if score1 >= 100:
    Label (window, text="Player 1 Wins!           ", bg="black", fg="white", font = "none 24 bold") .grid(row=1, column=5, sticky=W)
if score2 >= 100:
    Label (window, text="Player 2 Wins!           ", bg="black", fg="white", font = "none 24 bold") .grid(row=1, column=5, sticky=W)

# I hope you see this, I really enjoyed this class in this semester. Despite knowing python, I learned quite a bit and I'm glad I took this class. And also, on behalf of my friends, sorry for being loud :)
window.mainloop()


