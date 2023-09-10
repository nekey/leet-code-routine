"""
Link to task: https://leetcode.com/problems/jump-game-ii/?envType=study-plan-v2&envId=top-interview-150
"""
from typing import List


class Solution:
    def jump_1(self, nums: List[int]) -> int:
        current_fuel = 0
        next_fuel = 0
        jump_count = 0
        for jump_fuel in nums[:-1]:
            if current_fuel == 0:
                current_fuel = max(jump_fuel, next_fuel - 1)
                jump_count += 1
                next_fuel = 0
            else:
                next_fuel = max(next_fuel - 1, jump_fuel)
                current_fuel -= 1
        return jump_count + 1 if current_fuel == 0 else jump_count

    def jump(self, nums: List[int]) -> int:
        current_fuel = 0
        next_fuel = 0
        jump_count = 0
        for jump_fuel in nums[:-1]:
            next_fuel = max(jump_fuel - current_fuel, next_fuel)
            if current_fuel == 0:
                current_fuel = next_fuel
                jump_count += 1
                next_fuel = 0
            current_fuel -= 1
        return jump_count

def check_result(nums: List[int], expected_result: int) -> None:
    result = Solution().jump(nums)
    assert result is expected_result


def test_jump():
    check_result(nums=[2,3,1,1,4], expected_result=2)
    check_result(nums=[2,3,0,1,4], expected_result=2)
    check_result(nums=[2,3,3,1,4,1], expected_result=2)
    check_result(nums=[2,0,1,1], expected_result=2)
    check_result(nums=[1,1,1,1], expected_result=3)
    check_result(nums=[0], expected_result=0)
