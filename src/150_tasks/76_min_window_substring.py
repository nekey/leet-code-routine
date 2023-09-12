"""
Link to task: https://leetcode.com/problems/minimum-window-substring/
"""
from collections import Counter


class SolutionOld:
    """Done, but slow solution:

    633ms Beats 8.17%of users with Python3
    17.26MB Beats 19.01%of users with Python3
    """

    def minWindow(self, s: str, t: str) -> str:
        p_left = None
        t_counter = Counter(t)
        found_counter = Counter()
        result = ""
        for p_right, ch_right in enumerate(s):
            if ch_right in t_counter:
                if p_left is None:
                    # first matched char is found, set p_left
                    p_left = p_right
                found_counter[ch_right] += 1

            # if found more chars than need and it is equals char on left pointer, move that to next key char
            if found_counter[ch_right] > t_counter[ch_right] and s[p_left] == ch_right:
                # update left pointer
                while p_left < p_right + 1:
                    if s[p_left] in t_counter:
                        if found_counter[s[p_left]] > t_counter[s[p_left]]:
                            found_counter[s[p_left]] -= 1
                        else:
                            break
                    p_left += 1

            # substring completely found, update result
            if found_counter >= t_counter:
                # update result
                if not result or p_right - p_left + 1 < len(result):
                    result = s[p_left : p_right + 1]
                # update left pointer
                while p_left < p_right + 1:
                    if s[p_left] in t_counter:
                        if found_counter[s[p_left]] > t_counter[s[p_left]]:
                            found_counter[s[p_left]] -= 1
                        else:
                            break
                    p_left += 1

        return result


class Solution:
    """Cute and better

    125ms Beats 60.82%of users with Python3
    17.16MB Beats 59.59%of users with Python3
    """

    def minWindow(self, s: str, t: str) -> str:
        t_counter, missing = Counter(t), len(t)
        p_left = 0
        result = ""
        for p_right, ch in enumerate(s, 1):
            missing -= t_counter[ch] > 0
            t_counter[ch] -= 1
            if not missing:
                while p_left < p_right and t_counter[s[p_left]] < 0:
                    t_counter[s[p_left]] += 1
                    p_left += 1
                if not result or len(result) > p_right - p_left:
                    result = s[p_left:p_right]
        return result


def check_result(s: str, t: str, expected: str):
    assert Solution().minWindow(s, t) == expected


def test_min_window():
    check_result(s="ADOBECODEBANC", t="ABC", expected="BANC")
    check_result(s="a", t="a", expected="a")
    check_result(s="a", t="aa", expected="")
    check_result(s="ttt1234t", t="tttt", expected="ttt1234t")
    check_result(s="tta1234attt", t="attt", expected="attt")
    check_result(s="ttt", t="tttt", expected="")
    check_result(s="aaaaaaaaaaaabbbbbcdd", t="abcdd", expected="abbbbbcdd")
