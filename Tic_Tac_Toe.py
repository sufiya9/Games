#    Funtion to print Tic Tac Toe Board
def print_Tic_Tac_Toe_Board(values):
    print("\n")

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |")

    print("\n")

# Function to print the score-board for the game

def print_scoreboard(score_board):
    print("\t----------------------------------------------")
    print("\t       SCOREBOARD FOR TIC-TAC-TOE      ")
    print("\t----------------------------------------------")

    players = list(score_board.keys())
    print("\t   ", players[0], "\t    ", score_board[players[0]])
    print("\t   ", players[1], "\t    ", score_board[players[1]])

    print("\t---------------                 -------------\n")

# Function to check if any player has won the game

def check_winner(player_position, current_player):

    # All possible winning combinations for the player
    winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    # Loop to check if any winning combination is satisfied or not
    for x in winning_combinations:
        if all(y in player_position[current_player] for y in x):

            # Return True if any winning combination satisfies
            return True
    # Return False if no combination is satisfied
    return False

# Function to check if the game is drawn

def check_draw(player_position):
    if len(player_position['X']) + len(player_position['O']) == 9:
        return True
    return False

# Function for a single game of Tic Tac Toe
def single_game(current_player):

    # Represents the Tic Tac Toe
    values = [' ' for x in range(9)]

    # Stores the positions occupied by X and O
    player_position = {'X': [], 'O': []}

    # Game Loop for a single game of Tic Tac Toe
    while True:
        print_Tic_Tac_Toe_Board(values)

       # Try Exception block for MOVE input
        try:
            print("Player ", current_player, " turn. Which box? : ", end="")
            move = int(input())
        except ValueError:
            print("Wrong Input!!! Try Again")
            continue

    # Sanity check for MOVE inout
        if move < 1 or move > 9:
            print("Wrong Input!!! Try Again")
            continue

        # Check if the box is not occupied already

        if values[move - 1] != ' ':
            print("The Place you have choosen is already filled. Try again!!")
            continue

        # Update game information
        # update board status

        values[move - 1] = current_player

        # update player positions
        player_position[current_player].append(move)


        # Check if the current player wins
        if check_winner(player_position, current_player):
            print_Tic_Tac_Toe_Board(values)
            print("Player ", current_player, " has won the game!!")
            print("\n")
            return current_player

        # Check if the game is drawn
        if check_draw(player_position):
            print_Tic_Tac_Toe_Board(values)
            print("Game Drawn")
            print("\n")
            return 'D'

        # Switch player moves
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'

if __name__== "__main__":

    print("Player 1 Details" )
    player1 = input("Enter the name of player 1: ")
    print("\n")
    print("Player 2 Details" )
    player2 = input("Enter the name of player 2: ")
    print("\n") 

    # Stores the player who chooses X and O
    current_player = player1

    # Stores the choice of players
    player_choice = {'X': "", 'O': ""}

    #Store the options
    options = ['X', 'O']

    # Stores the scoreboard details
    score_board = { player1: 0, player2: 0 }
    print_scoreboard(score_board)
    print("\n")

    # Game Loop for a single game of Tic Tac Toe
    # The game loop will run until the players want to exit
    while True:
        #player1 choice menu
        print("Turn to Choose for", current_player)
        print("Enter 1 for X")
        print("Enter 2 for O")
        print("Enter 3 for Exit")
    

        # Try Exception block for CHOICE input
        try:
            choice = int(input())
        except ValueError:
            print("Wrong Input!!! Try Again")
            continue


        #Conditoins for the player choice
        if choice == 1:
            player_choice['X'] = current_player
            if current_player == player1:
                player_choice['O'] = player2
            else:
                player_choice['O'] = player1
        
        elif choice == 2:
            player_choice['O'] = current_player
            if current_player == player1:
                player_choice['X'] = player2
            else:
                player_choice['X'] = player1

        elif choice == 3:
            print("final Score")
            print_scoreboard(score_board)
            print("\n")
            break

        else:
            print("Wrong Input!!! Try Again \n")
            

        # strores the winner in a single game of the TIC TAC TOE!!!
        winner = single_game(options[choice - 1])


        # scoreboard edit accordingly to the winner
        if winner != "D":
            player_won = player_choice[winner]
            score_board[player_won] = score_board[player_won] + 1

        print_scoreboard(score_board)
        #Switch players who choose X and O
        if current_player == player1:
            current_player == player2
        else:
            current_player == player1
        print("\n")





   

    