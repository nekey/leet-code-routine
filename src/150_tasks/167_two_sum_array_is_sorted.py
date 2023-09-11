"""
Link to task: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/?envType=study-plan-v2&envId=top-interview-150
"""

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        p_left, p_right = 0, len(numbers) - 1
        while p_left < p_right:
            if numbers[p_left] + numbers[p_right] < target:
                p_left += 1
            elif numbers[p_left] + numbers[p_right] > target:
                p_right -= 1
            else:
                return [p_left + 1, p_right + 1]


def check_result(numbers: list[int], target: int, expected: list[int]) -> None:
    assert Solution().twoSum(numbers, target) == expected


def test_two_sum():
    check_result(numbers=[2,7,11,15], target=9, expected=[1,2])
    check_result(numbers=[2,3,4], target=6, expected=[1,3])
    check_result(numbers=[-1,0], target=-1, expected=[1,2])

