from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) < 1:
            return ""
        if len(strs) == 1:
            return strs[0]

        previous_word = strs[0]
        candidate = []

        for word in strs[1:]:
            current_candidate = ""
            min_len = min(
                len(previous_word),
                len(word),
                len(candidate) if len(candidate) > 0 else float("inf"),
            )
            previous_word, word = previous_word[:min_len], word[:min_len]
            for ch_previous_word, ch_word in zip(previous_word, word):
                if ch_previous_word == ch_word:
                    current_candidate += ch_word
                else:
                    break
            candidate = current_candidate

            if candidate == "":
                return ""
            ch_previous_word = word

        return candidate
