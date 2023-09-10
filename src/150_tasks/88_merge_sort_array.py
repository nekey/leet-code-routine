"""
https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150
"""

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for idx in range(n):
            nums1[m + idx] = nums2[idx]
        nums1.sort()
        # why sort in python3 is fast?
        # it is [timsort|https://en.wikipedia.org/wiki/Timsort] , complexity O(n*log(n))
        # but array with 2 already sorted lists is similar to best case => complexity is similar to O(n)


def check_result(nums1, m, nums2, n, expected_result):
    nums1_copy = nums1[:]
    Solution().merge(nums1=nums1_copy, m=m, nums2=nums2, n=n)
    assert nums1_copy == expected_result


def test_merge():
    check_result(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3, expected_result=[1, 2, 2, 3, 5, 6])
    check_result(nums1=[1], m=1, nums2=[], n = 0, expected_result=[1])
    check_result(nums1=[0], m=0, nums2=[1], n = 1, expected_result=[1])
