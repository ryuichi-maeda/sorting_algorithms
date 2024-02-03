from typing import List

from sort_algorithm import SortAlgorithm


class SelectionSort(SortAlgorithm):
    def sort(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            minI = i
            for j in range(i + 1, len(nums)):
                if nums[minI] > nums[j]:
                    minI = j
            nums[i], nums[minI] = nums[minI], nums[i]
        return nums
