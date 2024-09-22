import math
import time

board = [' ' for _ in range(9)]

def print_board():
    for i in range(0, 9, 3):
        print(f'| {board[i]} | {board[i+1]} | {board[i+2]} |')

def is_winner(player):
    win_conditions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True

    return  False

def is_board_full():
    return ' ' not in board

def minimax(is_maximizing):
    if is_winner('O'):
        return 1
    elif is_winner('X'):
        return -1
    elif is_board_full():
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

def best_move():
    best_score = -math.inf
    move = 0

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

def player_move():
    while True:
        move = int(input('Enter move between (1-9):')) - 1
        if move < 0 or move > 8:
            print('Invalid move')
        elif board[move] != ' ':
            print('Invalid move')
        else:
            board[move] = 'X'
            break


print("Welcome to Tic-tac-Toe! You are 'X' and AI is 'O'")
print_board()

while True:
    player_move()
    print_board()

    if is_winner('X'):
        print('You win!')
        break
    elif is_board_full():
        print("It's a tie!")
        break

    print("AI is making a move...")
    time.sleep(5)
    ai_move = best_move()
    board[ai_move] = 'O'
    print_board()

    if is_winner('O'):
        print('AI wins!')
        break
    elif is_board_full():
        print("It's a tie!")
        break



