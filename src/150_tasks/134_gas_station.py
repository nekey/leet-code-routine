"""
Link to task: https://leetcode.com/problems/gas-station/?envType=study-plan-v2&envId=top-interview-150
"""
from typing import List


class Solution:
    def canCompleteCircuit_1(self, gas: List[int], cost: List[int]) -> int:
        left = 0
        fuel = 0
        for right in range(2*len(gas)):
            fuel += gas[right % len(gas)] - cost[right % len(gas)]
            if fuel < 0:
                if right + 1 > len(gas):
                    return -1
                fuel = 0
                left = right + 1
            if right - left >= len(gas):
                return left
        return -1  # unexpected return

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # x2 faster solution: if sum(gas) >= sum(cost), we have at least 1 garantied solution
        # => we don;t need to iterate twice
        if sum(gas) < sum(cost):
            return -1

        left, fuel = 0, 0
        for right in range(len(gas)):
            fuel += gas[right] - cost[right]
            if fuel < 0:
                fuel = 0
                left = right + 1
        return left


def check_result(gas, cost, expected):
    assert Solution().canCompleteCircuit(gas, cost) == expected


def test_can_complete_circuit():
    check_result(gas=[1,2,3,4,5], cost=[3,4,5,1,2], expected=3)
    check_result(gas=[2,3,4], cost=[3,4,3], expected=-1)
    check_result(gas=[2,3,5], cost=[3,4,3], expected=2)
