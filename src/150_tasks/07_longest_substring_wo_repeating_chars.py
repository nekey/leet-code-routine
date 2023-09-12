"""
Link to task: https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        p_left = 0
        uniq_chars = set(s[0])
        max_length = 0
        for ch in s[1:]:
            if ch in uniq_chars:
                max_length = max(max_length, len(uniq_chars))
                while ch in uniq_chars:
                    uniq_chars.remove(s[p_left])
                    p_left += 1
            uniq_chars.add(ch)
        return max(max_length, len(uniq_chars))


def check_result(s: str, expected: int) -> None:
    assert Solution().lengthOfLongestSubstring(s) == expected


def test_len_of_longest_substring():
    check_result(s="abcabcbb", expected=3)
    check_result(s="bbbbb", expected=1)
    check_result(s="pwwkew", expected=3)
    check_result(s="au", expected=2)
