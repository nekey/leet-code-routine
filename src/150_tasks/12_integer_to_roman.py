"""
Link to task: https://leetcode.com/problems/integer-to-roman/?envType=study-plan-v2&envId=top-interview-150
"""

ROMAN_CHARS = [
    ["I", "V", "X"],  # 1,5,10
    ["X", "L", "C"],  # 10,50,100
    ["C", "D", "M"],  # 100,500,1000
    ["M"],  # 1000
]


class Solution:
    def intToRoman(self, num: int) -> str:
        i = 0
        result = ""
        while num > 0:
            num, last_digit = divmod(num, 10)
            if last_digit == 9:
                result += ROMAN_CHARS[i][2] + ROMAN_CHARS[i][0]
            elif last_digit >= 5:
                result += ROMAN_CHARS[i][0] * (last_digit - 5) + ROMAN_CHARS[i][1]
            elif last_digit == 4:
                result += ROMAN_CHARS[i][1] + ROMAN_CHARS[i][0]
            else:
                result += ROMAN_CHARS[i][0] * last_digit
            i += 1
        return result[::-1]


def check_result(num, expected):
    assert Solution().intToRoman(num) == expected


def test_roman_to_integer():
    check_result(num=3, expected="III")
    check_result(num=58, expected="LVIII")
    check_result(num=1994, expected="MCMXCIV")
