class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrom = str()
        for idx, ch in enumerate(s):
            left_idx = idx - 1
            right_idx = idx + 1

            # When center is impair (one center)
            while left_idx >= 0 and right_idx < len(s) and s[left_idx] == s[right_idx]:
                palindrom = s[left_idx : right_idx + 1]

                if len(palindrom) > len(longest_palindrom):
                    longest_palindrom = palindrom

                left_idx -= 1
                right_idx += 1

            # When center is pair (two centers)
            left_idx = idx
            right_idx = idx + 1
            while left_idx >= 0 and right_idx < len(s) and s[left_idx] == s[right_idx]:
                palindrom = s[left_idx : right_idx + 1]

                if len(palindrom) > len(longest_palindrom):
                    longest_palindrom = palindrom

                left_idx -= 1
                right_idx += 1

        return s[0] if len(longest_palindrom) == 0 else longest_palindrom
