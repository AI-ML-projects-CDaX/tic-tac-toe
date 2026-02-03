import math

# Board
board = [' ' for _ in range(9)]

# Print board
def print_board():
    print()
    for i in range(0, 9, 3):
        print(board[i], '|', board[i+1], '|', board[i+2])
        if i < 6:
            print('--+---+--')
    print()

# Check winner
def check_winner(player):
    win_positions = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    return any(all(board[pos] == player for pos in combo) for combo in win_positions)

# Check draw
def is_draw():
    return ' ' not in board

# Minimax algorithm
def minimax(is_maximizing):
    if check_winner('O'):
        return 1
    if check_winner('X'):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

# AI move
def ai_move():
    best_score = -math.inf
    best_move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = 'O'

# Player move
def player_move():
    while True:
        move = int(input("Enter your move (0-8): "))
        if 0 <= move <= 8 and board[move] == ' ':
            board[move] = 'X'
            break
        else:
            print("Invalid move. Try again.")

# Main game loop
def play_game():
    print("Tic-Tac-Toe (You = X, AI = O)")
    print("Positions: 0 to 8")
    print_board()

    while True:
        player_move()
        print_board()
        if check_winner('X'):
            print(" You win!")
            break
        if is_draw():
            print(" It's a draw!")
            break

        ai_move()
        print("AI played:")
        print_board()
        if check_winner('O'):
            print(" AI wins!")
            break
        if is_draw():
            print("It's a draw!")
            break

play_game()
