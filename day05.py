import math


def find_row(code):
    """
    FBFBBFFRLR
    """
    l = 0
    h = 127
    i = 0
    try:
        while i < 7:
            letter = code[i]
            mid = math.ceil((l + h) / 2)
            if letter == "F":
                h = mid
            elif letter == "B":
                l = mid
            else:
                raise ValueError(f"Invalid input {letter} at position [0-indexed] {i}")
            i += 1
    except ValueError as e:
        print(e)

    print("row l -> ", l)
    return l


def find_col(code):
    """"""
    l = 0
    h = 7
    i = 7

    try:
        while i < 10:
            letter = code[i]
            mid = math.ceil((l + h) / 2)
            if letter == "L":
                h = mid
            elif letter == "R":
                l = mid
            else:
                raise ValueError(f"Invalid input {letter} at position [0-indexed] {i}")
            i += 1
    except ValueError as e:
        print(e)

    print("col l -> ", l)
    return l


def process_input():
    return open("input/day05_input.txt").readlines()


def fifth_helper(code="FBFBBFFRLR"):
    """
    """
    m, n = 8, 128
    board = [[0] * m for _ in range(n)]
    code_list = process_input()
    highest_id = float('-inf')
    for code in code_list:
        r = find_row(code)
        c = find_col(code)
        board[r][c] = 1
        id_val = (r * 8) + c
        print(f"id for {code} : {id_val}")
        highest_id = max(highest_id, id_val)
    # part 1
    print("result -> ", highest_id)

    # airline seat in 2D matrix
    print("board \n", board)

    # part 2
    row, col = find_seat(board, n, m)
    print("my id ", (row * 8) + col)


def find_seat(board, n_row, n_col):
    """"
    The idea is to start from the center and search towards the ends
    """
    # first half
    for i in reversed(range(n_row // 2)):
        for j in range(n_col):
            if board[i][j] == 0 and i != 0:
                return i, j

    # second half
    for i in range(n_row // 2, n_row):
        for j in range(n_col):
            if board[i][j] == 0:
                return i, j
