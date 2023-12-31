"""
Link to task: https://leetcode.com/problems/spiral-matrix/

37ms - Beats 72.64%of users with Python3
16.09MB - Beats 99.83%of users with Python3
"""


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result = []
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        while top <= bottom and left <= right:
            if top == bottom:
                result += matrix[top][left : right + 1]
                return result
            if left == right:
                result += [line[left] for line in matrix[top : bottom + 1]]
                return result
            result += matrix[top][left : right + 1]
            result += [line[right] for line in matrix[top + 1 : bottom + 1]]
            result += list(reversed(matrix[bottom][left:right]))
            result += [line[left] for line in matrix[bottom - 1 : top : -1]]
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        return result


def check_result(matrix, expected_spiral_order):
    assert Solution().spiralOrder(matrix) == expected_spiral_order


def test_spiral_order():
    check_result(
        matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        expected_spiral_order=[1, 2, 3, 6, 9, 8, 7, 4, 5],
    )
    check_result(
        matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
        expected_spiral_order=[1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
    )
    check_result(
        matrix=[[1]],
        expected_spiral_order=[1],
    )
