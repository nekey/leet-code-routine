"""
Link to task: https://leetcode.com/problems/reverse-words-in-a-string/?envType=study-plan-v2&envId=top-interview-150
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))

def check_result(s, expected):
    assert Solution().reverseWords(s) == expected


def test_do():
    check_result(s="a good   example", expected="example good a")
