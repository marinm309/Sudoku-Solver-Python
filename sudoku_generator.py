sudoku = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]


def print_bord(brd):
    for index, row in enumerate(brd):
        if index % 3 == 0:
            print('-------------------------')
        row_string = []
        for i, num in enumerate(row):
            if i % 3 == 0:
                row_string.append('|')
            row_string.append(str(num)) if num else row_string.append(' ')
            if i == 8:
                row_string.append('|')
        print(' '.join(row_string))
    print('-------------------------')


def find_free(brd):
    for row in range(len(brd)):
        for col in range(len(brd)):
            if brd[row][col] == 0:
                return (row, col)


def validate(brd, row, col, num):
    for i in range(len(brd[0])):
        if brd[row][i] == num and col != i:
            return False

    for i in range(len(brd)):
        if brd[i][col] == num and row != i:
            return False

    for i in range(row - row % 3, row - row % 3 + 3):
        for j in range(col - col % 3, col - col % 3 + 3):
            if brd[i][j] == num:
                return False
    return True


def solve(brd):
    find = find_free(brd)
    if not find:
        return True
    row, col = find
    for num in range(1, 10):
        if validate(brd, row, col, num):
            brd[row][col] = num
            if solve(brd):
                return True
            brd[row][col] = 0
    return False


print_bord(sudoku)
solve(sudoku)
print_bord(sudoku)
