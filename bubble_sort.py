from typing import List

from sort_algorithm import SortAlgorithm


class BubbleSort(SortAlgorithm):
    def sort(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums
