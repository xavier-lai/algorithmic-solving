from typing import List


class Solution:
    def NaivefindMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1) + len(nums2)
        mid = n // 2

        i = j = 0
        merged = []

        while i < len(nums1) and j < len(nums2) and len(merged) <= mid:
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        while i < len(nums1) and len(merged) <= mid:
            merged.append(nums1[i])
            i += 1
        while j < len(nums2) and len(merged) <= mid:
            merged.append(nums2[j])
            j += 1

        if n % 2 == 0:
            return (merged[-1] + merged[-2]) / 2
        else:
            return merged[-1]

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        is_pair = (n + m) % 2 == 0
        shorter = nums1 if n <= m else nums2
        longer = nums2 if n <= m else nums1

        # Binary search on the shorter array
        low, high = 0, len(shorter)
        while low <= high:
            # The idea is to find the correct partition where left are always shorter than right
            i = (low + high) // 2
            j = (n + m + 1) // 2 - i

            left_shorter = shorter[i - 1] if i > 0 else -float("inf")
            right_shorter = shorter[i] if i < len(shorter) else float("inf")
            left_longer = longer[j - 1] if j > 0 else -float("inf")
            right_longer = longer[j] if j < len(longer) else float("inf")

            if left_shorter > right_longer:
                high = i - 1
            elif left_longer > right_shorter:
                low = i + 1
            else:
                median = (
                    (max(left_shorter, left_longer) + min(right_shorter, right_longer))
                    / 2
                    if is_pair
                    else max(left_shorter, left_longer)
                )
                return median
