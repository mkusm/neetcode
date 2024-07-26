
def is_valid_sudoku(board: list[list[str]]) -> bool:
    for row in board:
        already_checked = set()
        for e in row:
            if e == '.':
                continue
            if e in already_checked:
                return False
            already_checked.add(e)

    for i in range(9):
        already_checked = set()
        for j in range(9):
            e = board[j][i]
            if e == '.':
                continue
            if e in already_checked:
                return False
            already_checked.add(e)

    for i in range(3):
        for j in range(3):
            already_checked = set()
            for k in range(3):
                for l in range(3):
                    e = board[i*3 + k][j*3 + l]
                    if e == '.':
                        continue
                    if e in already_checked:
                        return False
                    already_checked.add(e)
    return True



def test_is_valid_sudoku():
    board = [
        ["1","2",".",".","3",".",".",".","."],
        ["4",".",".","5",".",".",".",".","."],
        [".","9","8",".",".",".",".",".","3"],
        ["5",".",".",".","6",".",".",".","4"],
        [".",".",".","8",".","3",".",".","5"],
        ["7",".",".",".","2",".",".",".","6"],
        [".",".",".",".",".",".","2",".","."],
        [".",".",".","4","1","9",".",".","8"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    # assert is_valid_sudoku(board)

    board = [
        ["1","2",".",".","3",".",".",".","."],
        ["4",".",".","5",".",".",".",".","."],
        [".","9","1",".",".",".",".",".","3"],
        ["5",".",".",".","6",".",".",".","4"],
        [".",".",".","8",".","3",".",".","5"],
        ["7",".",".",".","2",".",".",".","6"],
        [".",".",".",".",".",".","2",".","."],
        [".",".",".","4","1","9",".",".","8"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    assert not is_valid_sudoku(board)


if __name__ == "__main__":
    test_is_valid_sudoku()
