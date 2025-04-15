# Random vs. Random Player for 100 games
import random
from random import randint
from mancala import Mancala

# win counters
p1counter = 0 # a counter for how many times player 1 wins
p2counter = 0 # a counter for how many times player 2 wins
tiecounter = 0 # a counter for how many times the players tie

# move counters
p1moves = 0
p2moves = 0

n = 100;

for i in range(n):
    game = Mancala() # creating a new game every time
    
    # play until someone wins
    while(game.winning_eval() == (False, -1)):  
        # determining player
        player = game.current_player
        
        if(player == 1):
            p1moves = p1moves + 1
        else:
            p2moves = p2moves + 1
            
            
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
    
print("Player 1 won " + str(p1counter/n * 100) + "% of the time.")
print("Player 2 won " + str(p2counter/n * 100) + "% of the time.")
print("Ties occurred " + str(tiecounter/n * 100) + "% of the time.")
print()

p1avgmoves = p1moves/n
p2avgmoves = p2moves/n

print("Player 1 won with an average of " + str(p1avgmoves) + " per game.")
print("Player 2 won with an average of " + str(p2avgmoves) + " per game.")