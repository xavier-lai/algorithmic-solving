from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_idx, right_idx = 0, len(height) - 1
        larger_candidate = 0

        while left_idx < right_idx:
            left = height[left_idx]
            right = height[right_idx]

            common_height = min(left, right)
            width = right_idx - left_idx
            candidate = common_height * width

            larger_candidate = (
                candidate if candidate > larger_candidate else larger_candidate
            )

            if left < right:
                left_idx += 1
            else:
                right_idx -= 1

        return larger_candidate
