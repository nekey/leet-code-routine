"""
Link to task: https://leetcode.com/problems/valid-sudoku/

101ms - Beats 69.50%of users with Python3
16.23MB - Beats 78.64%of users with Python3
"""
from collections.abc import Iterable


class InvalidSudokuException(Exception):
    ...


class Solution:
    @staticmethod
    def _validate_line(line: Iterable[str], initial: set | None = None):
        if initial is None:
            initial = set()
        for value in line:
            if value == ".":
                continue
            if value in initial:
                raise InvalidSudokuException
            else:
                initial.add(value)
        return initial

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        try:
            # check lines
            for line in board:
                self._validate_line(line)
            # check columns
            for i in range(len(board[0])):
                self._validate_line(line[i] for line in board)
            # check sub-boxes
            for line_idx in (0, 3, 6):
                for column_idx in (0, 3, 6):
                    buffer = set()
                    for line in board[line_idx : line_idx + 3]:
                        buffer = self._validate_line(line[column_idx : column_idx + 3], initial=buffer)
        except InvalidSudokuException:
            return False
        return True


def check_result(board: list[list[str]], expected_is_valid: bool):
    assert Solution().isValidSudoku(board) is expected_is_valid


def test_is_valid_sudoku():
    check_result(
        board=[
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ],
        expected_is_valid=True,
    )
    check_result(
        board=[
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ],
        expected_is_valid=False,
    )
    check_result(
        board=[
            [".", ".", ".", ".", "5", ".", ".", "1", "."],
            [".", "4", ".", "3", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", "3", ".", ".", "1"],
            ["8", ".", ".", ".", ".", ".", ".", "2", "."],
            [".", ".", "2", ".", "7", ".", ".", ".", "."],
            [".", "1", "5", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", "2", ".", ".", "."],
            [".", "2", ".", "9", ".", ".", ".", ".", "."],
            [".", ".", "4", ".", ".", ".", ".", ".", "."],
        ],
        expected_is_valid=False,
    )
