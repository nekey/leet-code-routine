"""
Link to task: https://leetcode.com/problems/longest-common-prefix/?envType=study-plan-v2&envId=top-interview-150
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        result = ""
        for chars in zip(*strs):
            if all(ch == chars[0] for ch in chars):
                result += chars[0]
            else:
                return result
        return result


def check_result(strs, expected):
    assert Solution().longestCommonPrefix(strs) == expected


def test_longest_common_prefix():
    check_result(strs=["flower","flow","flight"], expected="fl")
    check_result(strs=["dog","racecar","car"], expected="")
    check_result(strs=["test", "test"], expected="test")
    check_result(strs=["test"], expected="test")
