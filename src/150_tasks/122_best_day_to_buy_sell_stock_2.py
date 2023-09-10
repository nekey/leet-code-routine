"""
Link to task: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/?envType=study-plan-v2&envId=top-interview-150
"""
from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0
        for curr_day in range(1, len(prices)):
            if prices[curr_day] > prices[curr_day-1]:
                total_profit += (prices[curr_day] - prices[curr_day-1])
        return total_profit


def check_result(prices: List[int], expected_profit: int) -> None:
    profit = Solution().maxProfit(prices)
    assert profit == expected_profit


def test_max_profit():
    check_result(prices=[7,1,5,3,6,4], expected_profit=7)
    check_result(prices=[1,2,3,4,5], expected_profit=4)
    check_result(prices=[7,6,4,3,1], expected_profit=0)
