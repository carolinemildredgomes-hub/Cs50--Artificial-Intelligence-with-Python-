import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):

    x_count = 0
    o_count = 0

    for row in board:
        x_count += row.count(X)
        o_count += row.count(O)

    if x_count <= o_count:
        return X
    return O


def actions(board):

    possible = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] is EMPTY:
                possible.add((i, j))

    return possible


def result(board, action):

    if action not in actions(board):
        raise Exception("Invalid move")

    new_board = [row[:] for row in board]

    i, j = action

    new_board[i][j] = player(board)

    return new_board


def winner(board):

    lines = []

    lines.extend(board)

    for j in range(3):
        lines.append([
            board[0][j],
            board[1][j],
            board[2][j]
        ])

    lines.append([
        board[0][0],
        board[1][1],
        board[2][2]
    ])

    lines.append([
        board[0][2],
        board[1][1],
        board[2][0]
    ])

    for line in lines:
        if line[0] is not None and line.count(line[0]) == 3:
            return line[0]

    return None


def terminal(board):

    if winner(board) is not None:
        return True

    for row in board:
        if EMPTY in row:
            return False

    return True


def utility(board):

    win = winner(board)

    if win == X:
        return 1

    if win == O:
        return -1

    return 0


def max_value(board):

    if terminal(board):
        return utility(board)

    v = -math.inf

    for action in actions(board):
        v = max(v, min_value(result(board, action)))

    return v


def min_value(board):

    if terminal(board):
        return utility(board)

    v = math.inf

    for action in actions(board):
        v = min(v, max_value(result(board, action)))

    return v


def minimax(board):

    if terminal(board):
        return None

    current = player(board)

    if current == X:

        best_score = -math.inf
        best_move = None

        for action in actions(board):
            score = min_value(result(board, action))

            if score > best_score:
                best_score = score
                best_move = action

        return best_move

    else:

        best_score = math.inf
        best_move = None

        for action in actions(board):
            score = max_value(result(board, action))

            if score < best_score:
                best_score = score
                best_move = action

        return best_move
