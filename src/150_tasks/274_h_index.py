"""
Link to task: https://leetcode.com/problems/h-index/?envType=study-plan-v2&envId=top-interview-150
"""
import itertools
from collections import Counter
from typing import List


class Solution:
    def hIndex_1(self, citations: List[int]) -> int:
        # create counter with hack. citations, that > len(citations) counted with len(citations) value
        c = Counter()
        for citation in citations:
            if citation >= len(citations):
                c[len(citations)] += 1
            else:
                c[citation] += 1
        checked_citations = 0

        # walk on counter
        for citation_value in sorted(c.keys(), reverse=True):
            if c[citation_value] + checked_citations >= citation_value:
                if checked_citations <= citation_value <= checked_citations + c[citation_value]:
                    return citation_value
                else:
                    return checked_citations
            else:
                checked_citations += c[citation_value]
        return 0

    def hIndex(self, citations: List[int]) -> int:
        # try same with "counter sort" optimisation
        for idx, citation in enumerate(sorted(citations,reverse=True)):
            if idx + 1 > citation:
                return idx
        return len(citations)




def check_result(citations, expected_h_index):
    h_index = Solution().hIndex(citations)
    assert h_index == expected_h_index


def test_h_index():
    check_result(citations=[3,0,6,1,5], expected_h_index=3)
    check_result(citations=[1,3,1], expected_h_index=1)
    check_result(citations=[2,1,1,2,2,1], expected_h_index=2)
    check_result(citations=[7], expected_h_index=1)
    check_result(citations=[100,100,0], expected_h_index=2)
    check_result(citations=[0, 0], expected_h_index=0)

