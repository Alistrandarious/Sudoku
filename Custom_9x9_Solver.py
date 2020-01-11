board = 0

def create_and_solve():
    global board
    print('Hi and welcome to Sudoku Solver\n'
          'Please input line by line your puzzle.'
          '\nSeperate values with commas.'
          '\n0 = blank.\n\n')
    row_A = input('Please input row 1\n')
    numbers_A = list(map(int, row_A.split(',')))
    row_B = input('Please input row 2\n')
    numbers_B = list(map(int, row_B.split(',')))
    row_C = input('Please input row 3\n')
    numbers_C = list(map(int, row_C.split(',')))
    row_D = input('Please input row 4\n')
    numbers_D = list(map(int, row_D.split(',')))
    row_E = input('Please input row 5\n')
    numbers_E = list(map(int, row_E.split(',')))
    row_F = input('Please input row 6\n')
    numbers_F = list(map(int, row_F.split(',')))
    row_G = input('Please input row 7\n')
    numbers_G = list(map(int, row_G.split(',')))
    row_H = input('Please input row 8\n')
    numbers_H = list(map(int, row_H.split(',')))
    row_I = input('Please input row 9\n')
    numbers_I = list(map(int, row_I.split(',')))

    board = [
        numbers_A,
        numbers_B,
        numbers_C,
        numbers_D,
        numbers_E,
        numbers_F,
        numbers_G,
        numbers_H,
        numbers_I

    ]

    print_board(board)
    gamemode = input('Is this correct? Y / N')
    if gamemode == 'Y' or 'y' or 'yes' or 'Yes':
        print('Solved below:')
        solve(board)
        print_board(board)
    elif gamemode == 'N' or 'n' or 'no' or 'No':
        create_and_test()
    else:
        create_and_test()


def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -  ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None

create_and_solve()
