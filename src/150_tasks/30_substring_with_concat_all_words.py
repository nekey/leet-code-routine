"""
Link to task: https://leetcode.com/problems/substring-with-concatenation-of-all-words/
"""
from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        result = []
        word_size = len(words[0])
        words_counter = Counter(words)
        len_left_words = len(s) - word_size * len(words) + 1
        p_left_range = min(word_size, len_left_words)
        for p_left in range(p_left_range):
            keys_counter = Counter()
            p_mid = p_left
            for p_right in range(p_left, len(s), word_size):
                word_in_line = s[p_right : p_right + word_size]
                if word_in_line not in words:
                    # unexpected key => clear cache and move p_mod to p_right + 1
                    keys_counter = Counter()
                    p_mid = p_right + word_size
                else:
                    # move p_mid to need amount of expected keys
                    while word_in_line in keys_counter and keys_counter[word_in_line] == words_counter[word_in_line]:
                        mid_word = s[p_mid : p_mid + word_size]
                        keys_counter[mid_word] -= 1
                        p_mid += word_size
                    # add new key to Counter
                    keys_counter[word_in_line] += 1
                    if keys_counter == words_counter:
                        # concatenated substring found
                        result.append(p_mid)
                        mid_word = s[p_mid : p_mid + word_size]
                        keys_counter[mid_word] -= 1
                        p_mid += word_size
        return result


def check_result(s: str, words: list[str], expected: list[int]) -> None:
    assert sorted(Solution().findSubstring(s, words)) == sorted(expected)


def test_find_substring():
    check_result(s="barfoothefoobarman", words=["foo", "bar"], expected=[0, 9])
    check_result(s="wordgoodgoodgoodbestword", words=["word", "good", "best", "word"], expected=[])
    check_result(s="barfoofoobarthefoobarman", words=["bar", "foo", "the"], expected=[6, 9, 12])
    check_result(s="abcacacac", words=["a", "b", "c"], expected=[0, 1])
    check_result(s="abdccacacb", words=["a", "b", "c"], expected=[7])
    check_result(s="abcabc", words=["a", "b", "c"], expected=[0, 1, 2, 3])
    check_result(s="aabbccaabbccd", words=["aa", "bb", "cc"], expected=[0, 2, 4, 6])
    check_result(s="abbabba", words=["ab", "ba", "bb"], expected=[0, 1])
    check_result(s="wordgoodgoodgoodbestword", words=["word", "good", "best", "good"], expected=[8])
