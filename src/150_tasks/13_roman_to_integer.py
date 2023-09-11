"""
Link to task: https://leetcode.com/problems/roman-to-integer/?envType=study-plan-v2&envId=top-interview-150
"""

ROMAN_2_INT_MAP = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}
ROMAN_SUBS_MAP = {
    "I": "VX",
    "X": "LC",
    "C": "DM",
}


class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        i = 0
        while i < len(s):
            if (i < (len(s) - 1)) and (s[i] in ROMAN_SUBS_MAP) and (s[i + 1] in ROMAN_SUBS_MAP[s[i]]):
                result += ROMAN_2_INT_MAP[s[i + 1]] - ROMAN_2_INT_MAP[s[i]]
                i += 2
            else:
                result += ROMAN_2_INT_MAP[s[i]]
                i += 1
        return result


def check_result(roman_string, expected):
    assert Solution().romanToInt(roman_string) == expected


def test_roman_to_integer():
    check_result(roman_string="III", expected=3)
    check_result(roman_string="LVIII", expected=58)
    check_result(roman_string="MCMXCIV", expected=1994)
