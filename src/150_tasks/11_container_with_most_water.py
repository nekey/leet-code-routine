"""
Link to task: https://leetcode.com/problems/container-with-most-water/description/
"""


class Solution:
    def maxArea(self, height: list[int]) -> int:
        p_left, p_right = 0, len(height) - 1
        max_area = 0
        while p_left < p_right:
            area = min(height[p_left], height[p_right]) * (p_right - p_left)
            if area > max_area:
                max_area = area
            if height[p_left] <= height[p_right]:
                p_left += 1
            else:
                p_right -= 1
        return max_area


def check_result(height, expected):
    assert Solution().maxArea(height) == expected


def test_max_area():
    check_result(height=[1, 8, 6, 2, 5, 4, 8, 3, 7], expected=49)
    check_result(height=[1, 2], expected=1)
    check_result(height=[2, 3, 4, 5, 18, 17, 6], expected=17)
