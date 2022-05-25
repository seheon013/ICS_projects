from utilities import generate_piece, print_board
DEV_MODE = False


def main(game_board: [[int, ], ]) -> [[int, ], ]:
    """
    2048 main function, runs a game of 2048 in the console.

    Uses the following keys:
    w - shift up
    a - shift left
    s - shift down
    d - shift right
    q - ends the game and returns control of the console
    :param game_board: a 4x4 2D list of integers representing a game of 2048
    :return: returns the ending game board
    """
    # Initialize board's first cell
    # TODO: generate a random piece and location using the generate_piece function
    random_piece = generate_piece(game_board, DEV_MODE)
    add_piece(game_board, random_piece)
   
    # Initialize game state trackers
    game_state_tracker = game_over(game_board)
    
    # Game Loop
    while True :
        # TODO: Reset user input variable
        user_input = ""

        # TODO: Take computer's turn
        # place a random piece on the board
        # check to see if the game is over using the game_over function
        random_piece = generate_piece(game_board, DEV_MODE)
        add_piece(game_board, random_piece)
        if game_state_tracker == True :
            break

        # TODO: Show updated board using the print_board function
        print_board(game_board)
        
        # TODO: Take user's turn
        # Take input until the user's move is a valid key
        # if the user quits the game, print Goodbye and stop the Game Loop
        # Execute the user's move
        user_input = input()
        if user_input == "w" : # up
            game_board = move_up(game_board)
            
        elif user_input == "a" : #left
            game_board = move_left(game_board)
        elif user_input == "s" : #down
            game_board = move_down(game_board)
        elif user_input == "d" : # right
            game_board = move_right(game_board)
        elif user_input == "q" :
            print('Goodbye')
            break
        else :
            user_input = input()
        if win_over(game_board) == True:
            break
        # Check if the user wins
    return game_board

def add_piece(game_board, random_piece : {str: int, }) :
    """adding new piece on game board."""
    row = random_piece['row']
    col = random_piece['column']
    val = random_piece['value']
    game_board[row][col] = val
    
def move_up(game_board) :
    """move numbers to up side."""
    w1 = switch(game_board)
    w2 = move_left(w1)
    w3 = switch(w2)
    return w3

def move_left(game_board) :  
    """move numbers to left."""
    a1 = compress(game_board)
    a2 = merge(a1)
    a3 = compress(a2)
    return a3

def move_down(game_board) :
    """move numbers to down."""
    s1 = switch(game_board)
    s2 = move_right(s1)
    s3 = switch(s2)
    return s3

def move_right(game_board) :  
    """move numbers to right."""
    d1 = reverse(game_board)
    d2 = move_left(d1)
    d3 = reverse(d2)
    return d3

def compress(game_board) :  #ccompress all numbers to the left 
    """compress numbers to the left."""
    for count in range(3):
        for i in range(4):
            for u in range(3):
                if game_board[i][u] == 0 and game_board[i][u+1] != 0:
                    game_board[i][u] = game_board[i][u+1]
                    game_board[i][u+1] = 0
                
    return game_board 

def merge(game_board) : #같은수 합치기 OK
    """add numbers that are same."""
    for i in range(4):
        for u in range(3):
            if game_board[i][u] == game_board[i][u+1] and game_board[i][u] != 0 :
                game_board[i][u] = game_board[i][u] * 2
                game_board[i][u+1] = 0
                
    return game_board

def reverse(game_board) : #좌우반전 OK
    """reverse the board left-right"""
    for i in game_board:
        i.reverse()
    return game_board
    
def switch(game_board) : #교차 
    """switch column and row"""
    new_board = [[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]]
    for i in range(4):
        for u in range(4):
            new_board[i][u] = game_board[u][i]
    return new_board

def game_over(game_board: [[int, ], ]) -> bool: #game over requirement 
    """
    Query the provided board's game state.

    :param game_board: a 4x4 2D list of integers representing a game of 2048
    :return: Boolean indicating if the game is over (True) or not (False)
    """

    for i in range(4):  #check if the board is full
        for u in range(4):
            if(game_board[i][u]== 0):
                return False
 
    for i in range(3): #check if there is no numbers that can be merged
        for u in range(3): 
            if(game_board[i][u]== game_board[i + 1][u] or game_board[i][u]== game_board[i][u + 1]):
                return False
                
    return True
    # TODO: Loop over the board and determine if the game is over
    # TODO: Don't always return false
    
def win_over(game_board: [[int, ], ]) -> bool: 
    """win requirement."""
    for row in game_board:
        for column in row:
            if column == 2048:
                return True
    return False

if __name__ == "__main__":
    main([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]])
          