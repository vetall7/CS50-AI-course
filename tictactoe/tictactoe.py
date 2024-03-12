"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_counter = sum(i.count(X) for i in board)
    o_counter = sum(i.count(O) for i in board)
    if x_counter <= o_counter:
        return X
    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_var = set()
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if board[i][j] is EMPTY:
                actions_var.add((i, j))
    return actions_var


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action is None:
        raise "BAD MOVE"
    board_copy = copy.deepcopy(board)
    if board_copy[action[0]][action[1]] == EMPTY:
        board_copy[action[0]][action[1]] = player(board)
        return board_copy
    else:
        raise "BAD MOVE"


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # horizontal and vertical checking
    for index, row in enumerate(board):
        if all(element == X for element in row) or all(board[i][index] == X for i in range(0, 3)):
            return X
        elif all(element == O for element in row) or all(board[i][index] == O for i in range(0, 3)):
            return O
    # Check main diagonal (from top-left to bottom-right)
    if all(board[i][i] == X for i in range(len(board))):
        return X
    elif all(board[i][i] == O for i in range(len(board))):
        return O

    # Check other diagonal (from top-right to bottom-left)
    if all(board[i][len(board) - 1 - i] == X for i in range(len(board))):
        return X
    elif all(board[i][len(board) - 1 - i] == O for i in range(len(board))):
        return O
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not None or sum(i.count(EMPTY) for i in board) == 0


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    game_state = winner(board)
    if game_state == X:
        return 1
    elif game_state == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    best_action = None
    if player(board) == X:
        _, best_action = max_value(board)
    else:
        _, best_action = min_value(board)
    return best_action


def max_value(board, counter=0):
    if terminal(board):
        return utility(board), None
    v = -2
    best_action = None
    for action in actions(board):
        temp_v, _ = min_value(result(board, action), counter)
        v2 = v
        v = max(v, temp_v)
        if v != v2:
            best_action = action
        counter += 1
        if counter == 15:  # depth-limited
           return v, best_action
    return v, best_action


def min_value(board, counter=0):
    if terminal(board):
        return utility(board), None
    v = 2
    best_action = None
    for action in actions(board):
        temp_v, _ = max_value(result(board, action), counter)
        v2 = v
        v = min(v, temp_v)
        if v != v2:
            best_action = action
        counter += 1
        if counter == 15:  # depth-limited
           return v, best_action
    return v, best_action
