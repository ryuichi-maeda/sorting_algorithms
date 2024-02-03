from typing import List

from sort_algorithm import SortAlgorithm


class HeapSort(SortAlgorithm):
    def sort(self, nums: List[int]) -> List[int]:
        length = len(nums)
        for i in range(len(nums) // 2 - 1, -1, -1):
            self.heapify(nums, length, i)

        for i in range(len(nums) - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.heapify(nums, i, 0)
        return nums

    def heapify(self, nums: List[int], length: int, i: int) -> None:
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < length and nums[largest] < nums[l]:
            largest = l
        if r < length and nums[largest] < nums[r]:
            largest = r

        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]
            self.heapify(nums, length, largest)
