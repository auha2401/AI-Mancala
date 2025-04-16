import random
from random import randint

class Mancala:
    def __init__(self, pits_per_player=6, stones_per_pit = 4):
        """
        The constructor for the Mancala class defines several instance variables:

        pits_per_player: This variable stores the number of pits each player has.
        stones_per_pit: It represents the number of stones each pit contains at the start of any game.
        board: This data structure is responsible for managing the Mancala board.
        current_player: This variable takes the value 1 or 2, as it's a two-player game, indicating which player's turn it is.
        moves: This is a list used to store the moves made by each player. It's structured in the format (current_player, chosen_pit).
        p1_pits_index: A list containing two elements representing the start and end indices of player 1's pits in the board data structure.
        p2_pits_index: Similar to p1_pits_index, it contains the start and end indices for player 2's pits on the board.
        p1_mancala_index and p2_mancala_index: These variables hold the indices of the Mancala pits on the board for players 1 and 2, respectively.
        """
        self.pits_per_player = pits_per_player
        self.board = [stones_per_pit] * ((pits_per_player+1) * 2)  # Initialize each pit with stones_per_pit number of stones 
        self.players = 2
        self.current_player = 1
        self.moves = []
        self.p1_pits_index = [0, self.pits_per_player-1]
        self.p1_mancala_index = self.pits_per_player
        self.p2_pits_index = [self.pits_per_player+1, len(self.board)-1-1]
        self.p2_mancala_index = len(self.board)-1
        
        # Zeroing the Mancala for both players
        self.board[self.p1_mancala_index] = 0
        self.board[self.p2_mancala_index] = 0

    def display_board(self):
        """
        Displays the board in a user-friendly format
        """
        player_1_pits = self.board[self.p1_pits_index[0]: self.p1_pits_index[1]+1]
        player_1_mancala = self.board[self.p1_mancala_index]
        player_2_pits = self.board[self.p2_pits_index[0]: self.p2_pits_index[1]+1]
        player_2_mancala = self.board[self.p2_mancala_index]

        print('P1               P2')
        print('     ____{}____     '.format(player_2_mancala))
        for i in range(self.pits_per_player):
            if i == self.pits_per_player - 1:
                print('{} -> |_{}_|_{}_| <- {}'.format(i+1, player_1_pits[i], 
                        player_2_pits[-(i+1)], self.pits_per_player - i))
            else:    
                print('{} -> | {} | {} | <- {}'.format(i+1, player_1_pits[i], 
                        player_2_pits[-(i+1)], self.pits_per_player - i))
            
        print('         {}         '.format(player_1_mancala))
        turn = 'P1' if self.current_player == 1 else 'P2'
        print('Turn: ' + turn)
        
    def valid_move(self, pit):
        """
        Function to check if the pit chosen by the current_player is a valid move.
        """
        check = False
        
        # write your code here
        # if the pit is out of range or empty
        if(self.current_player == 1):
            if(pit <= self.pits_per_player):
                if(self.board[pit - 1] != 0):
                    check = True
        else:
            if(pit <= self.pits_per_player):
                if(self.board[pit + self.pits_per_player] != 0):
                    check = True
                    
        return check
        
    def random_move_generator(self):
        """
        Function to generate random valid moves with non-empty pits for the random player
        """
        # write your code here
        valid = False
        
        # generating a random valid move
        while(valid == False):
            move = randint(1, self.pits_per_player)
            valid = self.valid_move(move)
            
        return move
    
    def play(self, pit):
        """
        This function simulates a single move made by a specific player using their selected pit. It primarily performs three tasks:
        1. It checks if the chosen pit is a valid move for the current player. If not, it prints "INVALID MOVE" and takes no action.
        2. It verifies if the game board has already reached a winning state. If so, it prints "GAME OVER" and takes no further action.
        3. After passing the above two checks, it proceeds to distribute the stones according to the specified Mancala rules.

        Finally, the function then switches the current player, allowing the other player to take their turn.
        """
        # write your code here
        # print("Player", self.current_player, "chose pit:", pit)
        # checking if pit is valid
        test = self.valid_move(pit)
        if(test != True):
            print("INVALID MOVE")
            print()
            return self.board
        
        # print()
    
        # checking for winning state
        win = self.winning_eval()
        if(win == (True, 1) or win == (True, 2) or win == (True, -1)):
            # print("GAME OVER")
            return self.board
        
        # determining current player
        if(self.current_player == 1):
            self.moves.append((1, pit))
            moves = self.board[pit - 1]
            self.board[pit - 1] = 0 # adjusting current count
            for i in range(1, moves + 1):
                nextpit = (pit + i - 1) % (len(self.board))
                # make sure that pit is not opponent's mancala
                if(nextpit == self.p2_mancala_index):
                    nextpit = (nextpit + 1) % (len(self.board))
                self.board[nextpit] += 1 # deposting a marble
                # if on last move
                if(i == (moves)): 
                    if(self.board[nextpit] == 0): # empty
                        opp_pit = abs(self.pits_per_player - nextpit)
                        opp_pit = opp_pit + self.pits_per_player + 1 # adjusting to index
                        extras = self.board[opp_pit]
                        self.board[opp_pit] = 0
                        # place these in my mancala
                        self.board[self.p1_mancala_index] += extras
                        
            # switching to player 2
            self.current_player = 2
        else:
            self.moves.append((2, pit))
            # moving base pit up accordingly to be at the right index
            pit = pit + self.pits_per_player + 1
            moves = self.board[pit - 1]
            self.board[pit - 1] = 0 # adjusting current count
            for i in range(1, moves + 1):
                nextpit = (pit + i - 1) % (len(self.board))
                # make sure that pit is not opponent's mancala
                if(nextpit == self.p1_mancala_index):
                    nextpit = (nextpit + 1) % (len(self.board))
                self.board[nextpit] += 1 # deposting a marble
                # if on last move
                if(i == (moves)): 
                    if(self.board[nextpit] == 0): # empty
                        opp_pit = abs(self.pits_per_player - nextpit)
                        opp_pit = opp_pit -  1 # adjusting to index
                        extras = self.board[opp_pit]
                        self.board[opp_pit] = 0
                        # place these in my mancala
                        self.board[self.p2_mancala_index] += extras
                        
            # switching to player 1
            self.current_player = 1
                
        
        return self.board
    
    def winning_eval(self):
        """
        Function to verify if the game board has reached the winning state.
        Hint: If either of the players' pits are all empty, then it is considered a winning state.
        """
        # if a player's side is empty, the game is over, and whoever has the most stones in their mancala wins
        state = True
        
        for i in range(self.pits_per_player): # player one's side is empty
            if (self.board[i] != 0):
                state = False
                pl = -1
                
        if(state == True):
            # count the number of stones on player two's side, adding these to their mancala
            for i in range(self.pits_per_player):
                stones = self.board[self.pits_per_player + 1 + i]
                self.board[self.pits_per_player + 1 + i] = 0 # taking them out of the pits
                self.board[self.p2_mancala_index] = self.board[self.p2_mancala_index] + stones
                
            # determining who won
            if (self.board[self.p1_mancala_index] > self.board[self.p2_mancala_index]):
                # player one wins
                return (state, 1)
            elif (self.board[self.p2_mancala_index] > self.board[self.p1_mancala_index]):
                # player two wins
                return (state, 2)
            else:
                # tie
                return (state, -1)
    
        state = True
        for i in range(self.pits_per_player): # player two's side is empty
            if (self.board[self.pits_per_player + 1 + i] != 0):
                state = False
                pl = -1
                
        if (state == True):
            # count the number of stones on player one's side, adding these to their mancala
            for i in range(self.pits_per_player):
                stones = self.board[i]
                self.board[i] = 0
                self.board[self.p1_mancala_index] = self.board[self.p1_mancala_index] + stones
                
            # determining who won
            if (self.board[self.p1_mancala_index] > self.board[self.p2_mancala_index]):
                # player one wins
                return (state, 1)
            elif (self.board[self.p2_mancala_index] > self.board[self.p1_mancala_index]):
                # player two wins
                return (state, 2)
            else:
                # tie
                return (state, -1)
        
        return (state, pl)
    
    def utility(self):
        return self.board[self.p1_mancala_index] - self.board[self.p2_mancala_index]
    
    def minimax(self, depth, max_depth, maximizing_player):
        if depth == max_depth or self.winning_eval()[0]:
            return self.utility(), None

        if maximizing_player:  # Player 1 (Max)
            best_value = float('-inf')
            best_move = None
            for pit in range(1, self.pits_per_player + 1):
                if self.valid_move(pit):
                    game_copy = Mancala(self.pits_per_player, 0)
                    game_copy.board = self.board.copy()
                    game_copy.current_player = self.current_player
                    game_copy.play(pit)
                    value, _ = game_copy.minimax(depth + 1, max_depth, False)
                    if value > best_value:
                        best_value = value
                        best_move = pit
            return best_value, best_move
        else:  # Player 2 (Min)
            best_value = float('inf')
            best_move = None
            for pit in range(1, self.pits_per_player + 1):
                if self.valid_move(pit):
                    game_copy = Mancala(self.pits_per_player, 0)
                    game_copy.board = self.board.copy()
                    game_copy.current_player = self.current_player
                    game_copy.play(pit)
                    value, _ = game_copy.minimax(depth + 1, max_depth, True)
                    if value < best_value:
                        best_value = value
                        best_move = pit
            return best_value, best_move

    def get_best_move(self, max_depth):
        _, move = self.minimax(0, max_depth, self.current_player == 1)
        return move 
    
    def alpha_beta(self, depth, alpha, beta, max_depth, maximizing_player):
        if depth == max_depth or self.winning_eval()[0]:
            return self.utility(), None

        if maximizing_player:  # Player 1 (Max)
            best_value = float('-inf')
            best_move = None
            for pit in range(1, self.pits_per_player + 1):
                if self.valid_move(pit):
                    game_copy = Mancala(self.pits_per_player, 0)
                    game_copy.board = self.board.copy()
                    game_copy.current_player = self.current_player
                    game_copy.play(pit)
                    value, _ = game_copy.alpha_beta(depth + 1, alpha, beta, max_depth, False)
                    if value > best_value:
                        best_value = value
                        best_move = pit
                    alpha = max(alpha, best_value)
                    
                    # alpha beta pruning
                    if beta <= alpha:
                        break
                        
            return best_value, best_move
        else:  # Player 2 (Min)
            best_value = float('inf')
            best_move = None
            for pit in range(1, self.pits_per_player + 1):
                if self.valid_move(pit):
                    game_copy = Mancala(self.pits_per_player, 0)
                    game_copy.board = self.board.copy()
                    game_copy.current_player = self.current_player
                    game_copy.play(pit)
                    value, _ = game_copy.alpha_beta(depth + 1, alpha, beta, max_depth, True)
                    if value < best_value:
                        best_value = value
                        best_move = pit
                    beta = min(beta, best_value)
                    
                    # alpha beta pruning
                    if beta <= alpha:
                        break
            return best_value, best_move
        
        
    def alpha_beta_move(self, max_depth):
        _, move = self.alpha_beta(0, float('-inf'), float('inf'), max_depth, self.current_player == 1)
        return move
