"""
Link to task: https://leetcode.com/problems/zigzag-conversion/?envType=study-plan-v2&envId=top-interview-150
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        sub_lines = ["" for _ in range(numRows)]
        slot_size = (numRows - 1) * 2
        for idx, ch in enumerate(s):
            sub_lines_idx = idx % slot_size if (idx % slot_size) < numRows else slot_size - (idx % slot_size)
            sub_lines[sub_lines_idx] += ch
        return "".join(sub_lines)


def check_result(s, num_rows, expected_str):
    assert Solution().convert(s=s, numRows=num_rows) == expected_str


def test_convert():
    check_result(s="PAYPALISHIRING", num_rows=3, expected_str="PAHNAPLSIIGYIR")
    check_result(s="PAYPALISHIRING", num_rows=4, expected_str="PINALSIGYAHRPI")
    check_result(s="PAYPALISHIRING", num_rows=5, expected_str="PHASIYIRPLIGAN")
    check_result(s="A", num_rows=1, expected_str="A")
    check_result(s="TEST", num_rows=1, expected_str="TEST")
