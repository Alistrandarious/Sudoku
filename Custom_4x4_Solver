board = 0

def create_and_test():
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

    board = [
        numbers_A,
        numbers_B,
        numbers_C,
        numbers_D
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

    for i in range(1, 5):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0
    return False


def print_board(bo):
    for i in range(len(bo)):
        if i % 2 == 0 and i != 0:
            print('------------')

        for j in range(len(bo[0])):
            if j % 2 == 0:
                print("| ", end='')

            if j == 3:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + ' ', end='')


def valid(bo, number, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == number and pos[1] != i:
            return False
    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == number and pos[0] != i:
            return False

    # Check box
    box_X = pos[1] // 2
    box_Y = pos[0] // 2

    for i in range(box_Y * 2, box_Y * 2 + 2):
        for j in range(box_X * 2, box_X * 2 + 2):
            if bo[i][j] == number and (i, j) != pos:
                return False

    return True


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col a.k.a y, x

    return None

create_and_test()
