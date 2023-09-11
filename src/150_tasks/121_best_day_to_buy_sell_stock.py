"""
Link to task: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=study-plan-v2
"""


class Solution:
    def maxProfit_1(self, prices: list[int]) -> int:
        # modified slight window algorithm
        # if current profit < 0 => forgot about all combinations that left that current right pointer
        # -> move left pointer to right and increment right one
        p_left = 0
        p_right = 1
        max_profit = 0
        while p_right < len(prices):
            profit = prices[p_right] - prices[p_left]
            if profit < 0:
                p_left = p_right
                p_right = p_left + 1
            else:
                max_profit = max(max_profit, profit)
                p_right += 1
        return max_profit

    def maxProfit(self, prices: list[int]) -> int:
        # less memory usage: combine comparison and var saving (use min and max)
        best_buy = prices[0]
        max_profit = 0
        for current_sell in prices[1:]:
            best_buy = min(best_buy, current_sell)
            max_profit = max(max_profit, current_sell - best_buy)
        return max_profit


def check_result(prices: list[int], expected_profit: int) -> None:
    profit = Solution().maxProfit(prices)
    assert profit == expected_profit


def test_max_profit():
    check_result(prices=[7, 1, 5, 3, 6, 4], expected_profit=5)
    check_result(prices=[7, 6, 4, 3, 1], expected_profit=0)
