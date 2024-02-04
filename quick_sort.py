from typing import List

from sort_algorithm import SortAlgorithm


class QuickSort(SortAlgorithm):
    def median_of_three(self, nums: List[int], l, r) -> int:
        m = l + (r - l) // 2
        x, y, z = nums[l], nums[m], nums[r]
        if x > y:
            if y > z:
                return m
            elif z > x:
                return l
            else:
                return r
        else:
            if x > z:
                return l
            elif z > y:
                return m
            else:
                return r

    def partition(self, nums: List[int], l: int, r: int, pivot: int) -> int:
        i = l - 1
        for j in range(l, r):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]

        # pivot is moved to the boundary
        nums[i + 1], nums[r] = nums[r], nums[i + 1]
        return i + 1

    def quick_sort(self, nums: List[int], l: int, r: int):
        if l >= r:
            return
        pivot_i = self.median_of_three(nums, l, r)
        pivot = nums[pivot_i]

        # pivot is moved to the end
        nums[r], nums[pivot_i] = nums[pivot_i], nums[r]

        partition_i = self.partition(nums, l, r, pivot)
        self.quick_sort(nums, l, partition_i - 1)
        self.quick_sort(nums, partition_i + 1, r)

    def sort(self, nums: List[int]) -> List[int]:
        self.quick_sort(nums, 0, len(nums) - 1)
        return nums
