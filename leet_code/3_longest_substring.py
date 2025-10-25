class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0

        known_letters = {}
        current_substring = str()
        longest_substring = str()
        current_start_idx = 0

        for idx, letter in enumerate(s):
            known_idx = known_letters.get(letter)
            if known_idx is not None and known_idx >= current_start_idx:
                current_start_idx = known_idx + 1
                if len(current_substring) > len(longest_substring):
                    longest_substring = current_substring
                if known_idx + 1 < idx:
                    current_substring = s[current_start_idx : idx + 1]
                else:
                    current_substring = letter
            else:
                current_substring += letter

            known_letters[letter] = idx

        return (
            len(current_substring)
            if len(longest_substring) < len(current_substring)
            else len(longest_substring)
        )
