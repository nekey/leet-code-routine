"""
Link to task: https://leetcode.com/problems/length-of-last-word/?envType=study-plan-v2&envId=top-interview-150
"""


class Solution:
    def lengthOfLastWord_1(self, s: str) -> int:
        left = None
        for idx, ch in enumerate(reversed(s)):
            if ch != " " and left is None:
                left = idx
            if ch == " " and left is not None:
                return idx - left
        return len(s) - left

    def lengthOfLastWord(self, s: str) -> int:
        # python way
        return len(s.split()[-1])


def check_result(s, expected):
    assert Solution().lengthOfLastWord(s) == expected


def test_length_of_last_word():
    check_result(s="Hello World", expected=5)
    check_result(s="   fly me   to   the moon  ", expected=4)
    check_result(s="luffy is still joyboy", expected=6)
    check_result(s="s   ", expected=1)
    check_result(s="   s", expected=1)
