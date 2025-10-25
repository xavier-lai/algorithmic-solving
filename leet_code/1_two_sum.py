from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        known_value_dict = dict()
        for current_idx, current_value in enumerate(nums):
            if current_idx == 0:
                known_value_dict[current_value] = current_idx
                continue
            else:
                value_to_search = target - current_value
                idx_to_search = known_value_dict.get(value_to_search)
                if idx_to_search is not None:
                    return [current_idx, idx_to_search]
                known_value_dict[current_value] = current_idx


class NaiveSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_range = range(0, len(nums))
        for current_idx in index_range:
            for searching_idx in index_range:
                if current_idx != searching_idx:
                    if nums[current_idx] + nums[searching_idx] == target:
                        return [current_idx, searching_idx]


class IntermediateSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_sorted = sorted(nums)
        left_pointer = 0
        right_pointer = len(nums_sorted) - 1

        while left_pointer < right_pointer:
            current_sum = nums_sorted[left_pointer] + nums_sorted[right_pointer]
            if current_sum == target:
                solution_value = [nums_sorted[left_pointer], nums_sorted[right_pointer]]
                break
            elif current_sum < target:
                left_pointer += 1
            else:
                right_pointer -= 1

        solution_idx = []
        for idx, value in enumerate(nums):
            if value == solution_value[0] or value == solution_value[1]:
                solution_idx.append(idx)

        return solution_idx
