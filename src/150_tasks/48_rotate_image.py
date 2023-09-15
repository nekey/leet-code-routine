"""
Link to task: https://leetcode.com/problems/rotate-image/
"""


class Solution1:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        46ms - Beats 37.40%of users with Python3
        16.28MB - Beats 82.83%of users with Python3
        Slow runtime :(
        """
        div_size, mod_size = divmod(len(matrix), 2)
        for row_id in range(div_size):
            for column_id in range(div_size + mod_size):
                (
                    matrix[row_id][column_id],
                    matrix[column_id][len(matrix) - row_id - 1],
                    matrix[len(matrix) - row_id - 1][len(matrix) - column_id - 1],
                    matrix[len(matrix) - column_id - 1][row_id],
                ) = (
                    matrix[len(matrix) - column_id - 1][row_id],
                    matrix[row_id][column_id],
                    matrix[column_id][len(matrix) - row_id - 1],
                    matrix[len(matrix) - row_id - 1][len(matrix) - column_id - 1],
                )


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        Dont know why, but it is faster
        37ms - Beats 88.14%of users with Python3
        16.29MB - Beats 82.83%of users with Python3
        """
        # step 1. transpose
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # set 2. flip vertically
        for row in range(len(matrix)):
            matrix[row].reverse()


def check_result(matrix: list[list[int]], expected: list[list[int]]) -> None:
    Solution().rotate(matrix)
    assert matrix == expected


def test_rotate():
    check_result(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], expected=[[7, 4, 1], [8, 5, 2], [9, 6, 3]])
    check_result(
        matrix=[[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],
        expected=[[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]],
    )
