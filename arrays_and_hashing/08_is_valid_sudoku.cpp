#include <iostream>
#include <vector>
#include <string>
#include <cassert>
#include <unordered_set>

using std::vector, std::string;

bool is_valid_sudoku(vector<vector<char>>& board)
{
	std::unordered_set<int> already_checked;

	for (int i = 0; i < 9; i++) {
		already_checked.clear();
		for (int j = 0; j < 9; j++) {
			int e = board[i][j];
			if (e == '.')
				continue;
			if (already_checked.find(e) != already_checked.end())
				return false;
			already_checked.insert(e);
		}
	}

	for (int i = 0; i < 9; i++) {
		already_checked.clear();
		for (int j = 0; j < 9; j++) {
			int e = board[j][i];
			if (e == '.')
				continue;
			if (already_checked.find(e) != already_checked.end())
				return false;
			already_checked.insert(e);
		}
	}

	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 3; j++) {
			already_checked.clear();
			for (int k = 0; k < 3; k++) {
				for (int l = 0; l < 3; l++) {
					int e = board[i*3 + k][j*3 + l];
					if (e == '.')
						continue;
					if (already_checked.find(e) != already_checked.end())
						return false;
					already_checked.insert(e);
				}
			}
		}
	}
	return true;
}

void test_is_valid_sudoku()
{
    vector<vector<char>> board;
	board = {
        {'1','2','.','.','3','.','.','.','.'},
        {'4','.','.','5','.','.','.','.','.'},
        {'.','9','8','.','.','.','.','.','3'},
        {'5','.','.','.','6','.','.','.','4'},
        {'.','.','.','8','.','3','.','.','5'},
        {'7','.','.','.','2','.','.','.','6'},
        {'.','.','.','.','.','.','2','.','.'},
        {'.','.','.','4','1','9','.','.','8'},
        {'.','.','.','.','8','.','.','7','9'},
    };
	assert(is_valid_sudoku(board));

	board[2][2] = '1';
	assert(!is_valid_sudoku(board));



	std::cout << "All tests passed" << std::endl;
}

int main()
{
	test_is_valid_sudoku();
	return 0;
}
