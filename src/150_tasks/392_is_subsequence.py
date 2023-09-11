"""
Link to task: https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=top-interview-150
"""

class SolutionOld:
    """Good solution, but not enough speed(beats 35%)
    """
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True
        s_iter = iter(s)  # iterator object
        s_last_ch = next(s_iter)  # first char in s
        for ch in t:
            if ch == s_last_ch:
                try:
                    s_last_ch = next(s_iter)
                except StopIteration:
                    return True
        return False


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p_s, p_t = 0, 0
        while p_s < len(s) and p_t < len(t):
            if t[p_t] == s[p_s]:
                p_s += 1
            p_t += 1
        return (p_s == len(s))


def check_result(s: str, t: str, expected: bool) -> None:
    assert Solution().isSubsequence(s, t) is expected


def test_is_subsequence():
    check_result(s="abc", t="ahbgdc", expected=True)
    check_result(s="axc", t="ahbgdc", expected=False)
    check_result(s="", t="test", expected=True)
    check_result(s="", t="", expected=True)
