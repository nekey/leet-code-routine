"""
Link to task: https://leetcode.com/problems/majority-element/?envType=study-plan-v2&envId=top-interview-150
"""
from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        return c.most_common(1)[0][0]


def check_result(nums, expected_m):
    m = Solution().majorityElement(nums)
    assert m == expected_m


def test_majority_element():
    check_result(nums=[3,2,3], expected_m=3)
    check_result(nums=[2,2,1,1,1,2,2], expected_m=2)
