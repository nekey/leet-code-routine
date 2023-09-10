"""
Link to task: https://leetcode.com/problems/text-justification/?envType=study-plan-v2&envId=top-interview-150
"""
from typing import List


class Solution:
    @staticmethod
    def _make_line(words_chunk, max_width):
        content_len = sum(len(word) for word in words_chunk)
        if len(words_chunk) == 1:
            return words_chunk[0].ljust(max_width)
        common_space_amount, large_space_span_count = divmod(max_width - content_len, len(words_chunk) - 1)
        result = ""
        for idx in range(len(words_chunk) - 1):
            result += words_chunk[idx]
            result += " " * (common_space_amount + 1 if idx <= large_space_span_count else common_space_amount)
        result += words_chunk[-1]
        return result

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        words_chunk = []
        words_chunk_min_len = 0
        for word in words:
            if len(word) + words_chunk_min_len + 1 > maxWidth:
                result.append(self._make_line(words_chunk, maxWidth))
                words_chunk = []
                words_chunk_min_len = 0
            words_chunk.append(word)
            words_chunk_min_len += (len(word) if words_chunk_min_len == 0 else len(word) + 1)
        if words_chunk:
            result.append(self._make_line(words_chunk, maxWidth))
        return result


def check_result(words, maxWidth, expected_justify):
    assert Solution().fullJustify(words, maxWidth) == expected_justify


def test_full_justify():
    check_result(
        words=["This", "is", "an", "example", "of", "text", "justification."],
        maxWidth=16,
        expected_justify=[
           "This    is    an",
           "example  of text",
           "justification.  "
        ],
    )
    check_result(
        words=["What","must","be","acknowledgment","shall","be"],
        maxWidth=16,
        expected_justify=[
          "What   must   be",
          "acknowledgment  ",
          "shall be        "
        ],
    )
    check_result(
        words=["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"],
        maxWidth=20,
        expected_justify=[
          "Science  is  what we",
          "understand      well",
          "enough to explain to",
          "a  computer.  Art is",
          "everything  else  we",
          "do                  "
        ],
    )
