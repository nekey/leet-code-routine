"""
Link to task: https://leetcode.com/problems/text-justification/?envType=study-plan-v2&envId=top-interview-150
"""


class SolutionOld:
    """My first solution. It works, but slowly then others"""

    @staticmethod
    def _make_common_line(words_chunk, max_width):
        content_len = sum(len(word) for word in words_chunk)
        if len(words_chunk) == 1:
            return words_chunk[0].ljust(max_width)
        common_space_amount, large_space_span_count = divmod(max_width - content_len, len(words_chunk) - 1)
        result = ""
        for idx in range(len(words_chunk) - 1):
            result += words_chunk[idx]
            result += " " * (common_space_amount + 1 if idx < large_space_span_count else common_space_amount)
        result += words_chunk[-1]
        return result

    @staticmethod
    def _make_last_line(words_chunk, max_width):
        return " ".join(words_chunk).ljust(max_width)

    def split_words_to_chunks(self, words: list[str], maxWidth: int) -> tuple[list[str], bool]:
        """Yield chunk of words with lenght < 16 and flag "is_last" - is it last line or not"""
        words_chunk = []
        words_chunk_min_len = 0
        for word in words:
            actual_width = len(word) + words_chunk_min_len + 1 if words_chunk_min_len else len(word)
            if actual_width > maxWidth:
                yield words_chunk, False
                words_chunk = []
                words_chunk_min_len = 0
            words_chunk.append(word)
            words_chunk_min_len += len(word) if words_chunk_min_len == 0 else len(word) + 1
        if words_chunk:
            yield words_chunk, True

    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        result = []
        for words_chunk, is_last in self.split_words_to_chunks(words, maxWidth):
            if is_last:
                result.append(self._make_last_line(words_chunk=words_chunk, max_width=maxWidth))
            else:
                result.append(self._make_common_line(words_chunk=words_chunk, max_width=maxWidth))
        return result


class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        result, chunk, content_letters_count = [], [], 0
        for word in words:
            if content_letters_count + len(word) + len(chunk) > maxWidth:
                for i in range(maxWidth - content_letters_count):
                    word_in_chunk_idx = i % (len(chunk) - 1 or 1)
                    chunk[word_in_chunk_idx] += " "
                result.append("".join(chunk))
                chunk, content_letters_count = [], 0
            chunk += [word]
            content_letters_count += len(word)
        return result + [" ".join(chunk).ljust(maxWidth)]


def check_result(words, maxWidth, expected_justify):
    assert Solution().fullJustify(words, maxWidth) == expected_justify


def test_full_justify():
    check_result(
        words=["This", "is", "an", "example", "of", "text", "justification."],
        maxWidth=16,
        expected_justify=["This    is    an", "example  of text", "justification.  "],
    )
    check_result(
        words=["What", "must", "be", "acknowledgment", "shall", "be"],
        maxWidth=16,
        expected_justify=["What   must   be", "acknowledgment  ", "shall be        "],
    )
    check_result(
        words=[
            "Science",
            "is",
            "what",
            "we",
            "understand",
            "well",
            "enough",
            "to",
            "explain",
            "to",
            "a",
            "computer.",
            "Art",
            "is",
            "everything",
            "else",
            "we",
            "do",
        ],
        maxWidth=20,
        expected_justify=[
            "Science  is  what we",
            "understand      well",
            "enough to explain to",
            "a  computer.  Art is",
            "everything  else  we",
            "do                  ",
        ],
    )
    check_result(
        words=["Listen", "to", "many,", "speak", "to", "a", "few."],
        maxWidth=6,
        expected_justify=[
            "Listen",
            "to    ",
            "many, ",
            "speak ",
            "to   a",
            "few.  ",
        ],
    )
