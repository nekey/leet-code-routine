"""
Link to task: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-150
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = 2
        for idx in range(2, len(nums)):
            if nums[idx] != nums[p-2]:
                nums[p] = nums[idx]
                p += 1
        return p


def check_result(nums, expected_k, expected_nums):
    k = Solution().removeDuplicates(nums)
    assert k == expected_k
    assert nums[:len(expected_nums)] == expected_nums


def test_remove_duplicates():
    check_result(nums=[1,1,1,2,2,3], expected_k=5, expected_nums=[1,1,2,2,3])
    check_result(nums=[0,0,1,1,1,1,2,3,3], expected_k=7, expected_nums=[0,0,1,1,2,3,3])
    check_result(nums=[0,1,2,3,3,3,3,4,4,4], expected_k=7, expected_nums=[0,1,2,3,3,4,4])
