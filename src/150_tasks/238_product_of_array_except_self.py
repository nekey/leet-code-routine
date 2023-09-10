"""
Link to task: https://leetcode.com/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=top-interview-150

[1,2,3,4]
[1,1] - [1,1,1,1]
[1,4] - [1,1,1,1]
[2,12] - [1,1,4,1]
[6,24] - [1,12,8,1]
[24,24] - [24,12,8,6]

"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        pre = 1
        post = 1
        for idx in range(len(nums)):
            result[idx] *= pre
            pre *= nums[idx]
            result[len(nums)-idx-1] *= post
            post *= nums[len(nums)-idx-1]
        return result


def check_result(nums, expected):
    result = Solution().productExceptSelf(nums)
    assert result == expected


def test_do():
    check_result(nums=[1,2,3,4], expected=[24,12,8,6])
    check_result(nums=[-1,1,0,-3,3], expected=[0,0,9,0,0])
