"""
Link to task: https://leetcode.com/problems/trapping-rain-water/?envType=study-plan-v2&envId=top-interview-150
"""
from typing import List


class Solution:
    def trap_1(self, height: List[int]) -> int:
        # Solution with O(n) space
        water_limits = [0] * len(height)
        left_max = 0
        right_max = 0
        result = 0
        for i in range(len(height)):
            if height[i] > left_max:
                left_max = height[i]
            elif height[i] < left_max:
                water_limits[i] = left_max
        for i in range(len(height)-1, -1, -1):
            if height[i] > right_max:
                right_max = height[i]
            elif height[i] < right_max and water_limits[i] != 0:
                result += min(right_max, water_limits[i]) - height[i]
        return result

    def trap(self, height: List[int]) -> int:
        # Solution with 2 pointers ( O(1) space )
        result = 0
        max_left, max_right = height[0], height[-1]
        left_p, right_p = 1, len(height) - 2
        while left_p <= right_p:
            if height[left_p] > max_left: max_left = height[left_p]
            if height[right_p] > max_right: max_right = height[right_p]

            if max_left <= max_right:
                result += (max_left - height[left_p])
                left_p += 1
            else:
                result += (max_right - height[right_p])
                right_p -= 1
        return result


def check_result(height, expected):
    assert Solution().trap(height) == expected


def test_trap():
    check_result(height=[0,1,0,2,1,0,1,3,2,1,2,1], expected=6)

