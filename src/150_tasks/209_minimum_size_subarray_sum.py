"""
Link to task: https://leetcode.com/problems/minimum-size-subarray-sum/
"""


class SolutionOld:
    """Slow solution (241ms Beats 36.81% of users with Python3)"""

    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        p_left, p_right = 0, 0
        min_sub_array_len = 0
        current_sum = nums[0]
        while True:
            if current_sum >= target:
                if min_sub_array_len == 0 or (p_right - p_left + 1) < min_sub_array_len:
                    min_sub_array_len = p_right - p_left + 1
                current_sum -= nums[p_left]
                p_left += 1
            else:
                p_right += 1
                if p_right == len(nums):
                    break
                current_sum += nums[p_right]
        return min_sub_array_len


class Solution:
    """20ms faster :D"""

    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        p_left, current_sum = 0, 0
        min_sub_array_len = 0
        for i in range(len(nums)):
            current_sum += nums[i]
            while current_sum >= target:
                if min_sub_array_len == 0 or (i - p_left + 1) < min_sub_array_len:
                    min_sub_array_len = i - p_left + 1
                current_sum -= nums[p_left]
                p_left += 1
        return min_sub_array_len


def check_result(target, nums, expected):
    assert Solution().minSubArrayLen(target, nums) == expected


def test_min_sub_array_len():
    check_result(target=7, nums=[2, 3, 1, 2, 4, 3], expected=2)
    check_result(target=4, nums=[1, 4, 4], expected=1)
    check_result(target=11, nums=[1, 1, 1, 1, 1], expected=0)
