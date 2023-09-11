"""
Link to task: https://leetcode.com/problems/jump-game/?envType=study-plan-v2&envId=top-interview-150
"""


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        current_fuel = 0
        for jump_fuel in nums[:-1]:
            current_fuel = max(current_fuel, jump_fuel) - 1
            if current_fuel < 0:
                return False
        return True


def check_result(nums: list[int], expected_result: bool) -> None:
    result = Solution().canJump(nums)
    assert result is expected_result


def test_can_jump():
    check_result(nums=[2, 3, 1, 1, 4], expected_result=True)
    check_result(nums=[3, 2, 1, 0, 4], expected_result=False)
