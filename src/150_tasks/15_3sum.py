"""
Link to task: https://leetcode.com/problems/3sum/?envType=study-plan-v2&envId=top-interview-150
"""
from collections import Counter


class SolutionOld:
    """Works, but too slow (6696ms Beats 5.00%)

    """
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()
        for p_left in range(len(nums) - 2):
            if nums[p_left] > 0:
                break
            p_mid, p_right = p_left + 1, len(nums) - 1
            while p_mid < p_right:
                current_sum = sum((nums[p_left], nums[p_mid], nums[p_right]))
                if current_sum == 0 and [nums[p_left], nums[p_mid], nums[p_right]] not in result:
                    result.append([nums[p_left], nums[p_mid], nums[p_right]])
                if current_sum < 0:
                    p_mid += 1
                else:
                    p_right -= 1
        return result


class Solution:
    """
    Not best solution, but ok: 1333ms Beats 47.03%of users with Python3
    """
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []

        # split nums to positive/negative/zero counters
        positive_counter = Counter()
        negative_counter = Counter()
        zero_count = 0
        for num in nums:
            if num > 0:
                positive_counter[num] += 1
            elif num < 0:
                negative_counter[num] += 1
            else:
                zero_count += 1

        # handle zeroes
        if zero_count >= 3:
            result.append([0, 0, 0])
        if zero_count >= 1:
            for positive_value in positive_counter.keys():
                if -positive_value in negative_counter:
                    result.append([-positive_value, 0, positive_value])

        uniq_negatives = sorted(negative_counter.keys())
        uniq_positives = sorted(positive_counter.keys())

        # check multiply by 2
        for counter_left, counter_right in ((negative_counter, positive_counter), (positive_counter, negative_counter)):
            for (value, count) in counter_left.items():
                if count > 1 and value * (-2) in counter_right:
                    result.append(sorted([value, value, value * (-2)]))

        # check uniq combo 2negative+1positive/ 2positive+1negative
        for two_num, one_num in ((uniq_negatives, uniq_positives), (uniq_positives, uniq_negatives)):
            for num in one_num:
                p_left, p_right = 0, len(two_num) - 1
                while p_left < p_right:
                    if num + two_num[p_left] + two_num[p_right] == 0:
                        result.append(sorted([num, two_num[p_left], two_num[p_right]]))
                    if num + two_num[p_left] + two_num[p_right] < 0:
                        p_left += 1
                    else:
                        p_right -= 1

        return result


def check_result(nums: list[int], expected: list[list[int]]) -> None:
    assert sorted(Solution().threeSum(nums)) == sorted(expected)


def test_three_sum():
    check_result(nums=[-1,0,1,2,-1,-4], expected=[[-1,-1,2],[-1,0,1]])
    check_result(nums=[0, 1, 1], expected=[])
    check_result(nums=[0, 0, 0], expected=[[0,0,0]])
    check_result(nums=[-2, -2, -2, -1, -1, -1, 2, 3], expected=[[-2, -1, 3], [-1, -1, 2]])
    check_result(nums=[-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6], expected=[[-4,-2,6],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]])

