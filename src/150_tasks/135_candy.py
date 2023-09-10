"""
Link to task: https://leetcode.com/problems/candy/?envType=study-plan-v2&envId=top-interview-150
"""
from enum import Enum
from typing import List


class Direction(Enum):
    EQ = 0
    UP = 1
    DOWN = 2


class Solution:
    def candy_1(self, ratings: List[int]) -> int:
        # My first try to do it in O(1). not success =(
        total_candies = 1
        last_direction = Direction.EQ
        direction_seq = 0

        for i in range(len(ratings) - 1):
            if ratings[i] == ratings[i+1]:
                current_direction = Direction.EQ
            elif ratings[i] < ratings[i+1]:
                current_direction = Direction.UP
            else:
                current_direction = Direction.DOWN

            if current_direction == Direction.EQ:
                total_candies += 1
                direction_seq = 0
            if (current_direction != Direction.EQ) and (last_direction == Direction.EQ):
                total_candies += 2
                direction_seq = 1
            if (
                    (last_direction == Direction.UP) and (current_direction == Direction.UP)
                    or (last_direction == Direction.DOWN) and (current_direction == Direction.DOWN)
            ):
                direction_seq += 1
                total_candies += (1+direction_seq)
            if (current_direction == Direction.UP) and (last_direction == Direction.DOWN):
                total_candies += 2
                direction_seq = 1
            if (current_direction == Direction.DOWN) and (last_direction == Direction.UP):
                total_candies += 1
                direction_seq = 1

            last_direction = current_direction
        return total_candies


    def candy(self, ratings: List[int]) -> int:
        given_candies = [1] * len(ratings)
        for i in range(len(ratings) - 1):
            # give more candies to right candidate if his rating is greater
            if ratings[i+1] > ratings[i]:
                given_candies[i+1] = given_candies[i] + 1
        for i in range(len(ratings) - 1, 0, -1):
            # give more candies to left candidate if his rating is greater
            if (ratings[i-1] > ratings[i]) and (given_candies[i-1] <= given_candies[i]):
                given_candies[i-1] = given_candies[i] + 1
        return sum(given_candies)



# 1 -> 1
# 2 -> 1+2=3 = 1+2
# 3 -> 1+2+3=6 4*3/2
# (1 + n)*n/2



def check_result(ratings, expected):
    assert Solution().candy(ratings) == expected


def test_candy():
    check_result(ratings=[1,0,2], expected=5)  # 2-1-2  # -1,1
    check_result(ratings=[1,2,2], expected=4)  # 1-2-1  # 1,0
    check_result(ratings=[1,2,2,2], expected=5)  # 1-2-1-1  # 1,0,0
    check_result(ratings=[1,2,3,3,2], expected=9)  # 1-2-3-2-1  # 1,1,0,-1
    check_result(ratings=[1,2,2,2,3], expected=7)  # 1-2-1-1-2  # 1,0,0,1
    check_result(ratings=[1,2,2,3], expected=6)  # 1-2-1-2  # 1,0,1
    check_result(ratings=[3,2,1], expected=6)  # 3-2-1  # -1,-1
    check_result(ratings=[3,2,2,1], expected=6)  # 2-1-2-1  # -1,0,-1
    check_result(ratings=[3,2,2,2,1], expected=7)  # 2-1-1-2-1  # -1,0,0,-1
    check_result(ratings=[1,2,2,1], expected=6)  # 1-2-2-1
    check_result(ratings=[1,2,2,3], expected=6)  # 1-2-1-2
    check_result(ratings=[3,2,2,1], expected=6)  # 2-1-1-2
    check_result(ratings=[1,2,3,1,0], expected=9)  # 1-2-3-2-1  # 1,1,0,-1


