# https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new_idx = 0
        for idx in range(len(nums)):
            if nums[idx] != val:
                nums[new_idx] = nums[idx]
                new_idx += 1
        return new_idx


def check_result(nums, val, expected_k, expected_nums):
    k = Solution().removeElement(nums=nums, val=val)
    assert k == expected_k
    assert set(nums[:len(expected_nums)]) == set(expected_nums)


def test_remove_element():
    check_result(nums=[3,2,2,3], val=3, expected_k=2, expected_nums=[2,2])
    check_result(nums=[0,1,2,2,3,0,4,2], val=2, expected_k=5, expected_nums=[0,1,4,0,3])
