"""
Link to task: https://leetcode.com/problems/rotate-array/?envType=study-plan-v2&envId=top-interview-150
"""
from typing import List


class Solution:
    # def rotate(self, nums: List[int], k: int) -> None:
    #     for _ in range(k):
    #         nums.insert(0, nums.pop())

    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]


def check_result(nums, k, expected_nums):
    Solution().rotate(nums, k)
    assert nums == expected_nums


def test_rotate():
    check_result(nums=[1,2,3,4,5,6,7], k=3, expected_nums=[5,6,7,1,2,3,4])
    check_result(nums=[-1,-100,3,99], k=2, expected_nums=[3,99,-1,-100])
    check_result(nums=[1,2], k=3, expected_nums=[2,1])
