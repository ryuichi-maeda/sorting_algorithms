from typing import List

from sort_algorithm import SortAlgorithm


class MergeSort(SortAlgorithm):
    def merge_sort(self, nums: List[int], l: int, r: int) -> List[int]:
        if l >= r:
            return [nums[l]]

        m = l + (r - l) // 2
        nums_l = self.merge_sort(nums, l, m)
        nums_r = self.merge_sort(nums, m + 1, r)

        res = []
        i, j = 0, 0
        while i < len(nums_l) and j < len(nums_r):
            if nums_l[i] < nums_r[j]:
                res.append(nums_l[i])
                i += 1
            else:
                res.append(nums_r[j])
                j += 1

        if i < len(nums_l):
            res += nums_l[i:]
        else:
            res += nums_r[j:]
        return res

    def sort(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        res = self.merge_sort(nums, 0, len(nums) - 1)
        return res

    def sort_with_single_method(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        l, r = 0, len(nums) - 1
        m = l + (r - l) // 2
        nums_l = self.sort(nums[: m + 1])
        nums_r = self.sort(nums[m + 1 :])

        res = []
        i, j = 0, 0
        while i < len(nums_l) and j < len(nums_r):
            if nums_l[i] < nums_r[j]:
                res.append(nums_l[i])
                i += 1
            else:
                res.append(nums_r[j])
                j += 1

        if i < len(nums_l):
            res += nums_l[i:]
        else:
            res += nums_r[j:]
        return res
