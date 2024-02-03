from typing import List

from sort_algorithm import SortAlgorithm


class InsertionSort(SortAlgorithm):
    def sort(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            target = nums[i]
            j = i - 1
            while j >= 0 and nums[j] > target:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = target
        return nums
