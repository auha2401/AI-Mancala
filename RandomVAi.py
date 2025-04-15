import random
from random import randint
from mancala import Mancala


ai_wins = 0  
random_wins = 0  
ties = 0

# Move counters
ai_moves = 0
random_moves = 0

max_depth = 5  # Number of plies

for i in range(100):
    game = Mancala()
    while(game.winning_eval() == (False, -1)):
        player = game.current_player
        if player == 1:  # AI minimax player
            move = game.get_best_move(max_depth)
            ai_moves += 1
        else:  # Random player
            move = game.random_move_generator()
            random_moves += 1
        game.play(move)
        # game.display_board()
        # print()

    win = game.winning_eval()
    
    if (win == (True, 1)):
        ai_wins += 1
    elif (win == (True, 2)):
        random_wins += 1
    else:
        ties += 1
        
    del game # removing the game for the next round
        
    # print()
    # print()

print(f"AI (Player 1) won {ai_wins}% of the time.")
print(f"Random (Player 2) won {random_wins}% of the time.")
print(f"Ties occurred {ties}% of the time.")
print()

p1avgmoves = ai_moves/100
p2avgmoves = random_moves/100

print("Player 1 won with an average of " + str(p1avgmoves) + " moves per game.")
print("Player 2 won with an average of " + str(p2avgmoves) + " moves per game.")