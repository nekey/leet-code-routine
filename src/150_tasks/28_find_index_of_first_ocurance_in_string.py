"""
Link to task: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/?envType=study-plan-v2
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            return haystack.index(needle)
        except ValueError:
            return -1


def check_result(haystack, needle, expected_idx):
    assert Solution().strStr(haystack, needle) == expected_idx


def test_str_str():
    check_result(haystack="sadbutsad", needle="sad", expected_idx=0)
    check_result(haystack="leetcode", needle="leeto", expected_idx=-1)
