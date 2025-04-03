# Random vs. Random Player for 100 games
import random
from random import randint
from mancala import Mancala

p1counter = 0; # a counter for how many times player 1 wins
p2counter = 0; # a counter for how many times player 2 wins
tiecounter = 0; # a counter for how many times the players tie

for i in range(100):
    game = Mancala() # creating a new game every time
    
    # play until someone wins
    while(game.winning_eval() == (False, -1)):  
        # player 1 plays
        game.play(game.random_move_generator())
        # print()
        # game.display_board()

        # player 2 plays
        game.play(game.random_move_generator())
        # print()
        # game.display_board()
        
    # someone won - determine who
    win = game.winning_eval()
    
    if (win == (True, 1)):
        p1counter = p1counter + 1
    elif (win == (True, 2)):
        p2counter = p2counter + 1
    else:
        tiecounter = tiecounter + 1
        
    del game # removing the game for the next round
        
    # print()
    # print()
    
print("Player 1 won " + str(p1counter) + "% of the time.")
print("Player 2 won " + str(p2counter) + "% of the time.")
print("Ties occurred " + str(tiecounter) + "% of the time.")