"""
Link to task: https://leetcode.com/problems/zigzag-conversion/?envType=study-plan-v2&envId=top-interview-150
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        sub_lines = ["" for _ in range(numRows)]
        slot_size = (numRows-1)*2
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


"""
P   A   H   N
A P L S I I G
Y   I   R


P     I    N
A   L S  I G
Y A   H R
P     I

P     H
A   S I
Y  I  R
P L   I G
A     N

0   4   8    12
1 3 5 7 9 11 13
2   6   10

0     6     12
1   5 7  11 13
2 4   8 10
3     9

0     8
1   7 9
2  6  10
3 5   11 13
4     12

# --

0   4   8     12
 1 3 5 7 9  11  13
  2   6   10

0     6       12       
 1   5 7    11  13
  2 4   8 10
   3     9
   

0       8
 1     7 9
  2   6   10
   3 5      11  13
    4         12


num_rows = 2 -> 2
num_rows = 3 -> 4
num_rows = 4 -> 6
num_rows = 5 -> 8

P = (num_rows-1)*2
f[0] => i % P == 0
f[1] => i % P == 1 or i % P == P - i



"""
