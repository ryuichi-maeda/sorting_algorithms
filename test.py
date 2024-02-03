import unittest
from heap_sort import HeapSort
from merge_sort import MergeSort
from selection_sort import SelectionSort

from sort_algorithm import SortAlgorithm
from bubble_sort import BubbleSort
from insertion_sort import InsertionSort


class SortTest(unittest.TestCase):
    def setUp(self):
        if self.__class__.__name__ == "SortTest":
            raise unittest.SkipTest("Base class")
        self.sort_algorithm: SortAlgorithm = self.get_sort_algorithm()

    def get_sort_algorithm(self):
        raise NotImplementedError

    def test_empty_list(self):
        self.assertEqual(self.sort_algorithm.sort([]), [])

    def test_already_sorted(self):
        self.assertEqual(self.sort_algorithm.sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        self.assertEqual(self.sort_algorithm.sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_random_order(self):
        self.assertEqual(self.sort_algorithm.sort([3, 1, 4, 5, 2]), [1, 2, 3, 4, 5])

    def test_duplicate_elements(self):
        self.assertEqual(self.sort_algorithm.sort([3, 3, 2, 1, 2]), [1, 2, 2, 3, 3])


class BubbleSortTest(SortTest):
    def get_sort_algorithm(self):
        return BubbleSort()


class InsertionSortTest(SortTest):
    def get_sort_algorithm(self):
        return InsertionSort()


class SelectionSortTest(SortTest):
    def get_sort_algorithm(self):
        return SelectionSort()


class HeapSortTest(SortTest):
    def get_sort_algorithm(self):
        return HeapSort()


class MergeSortTest(SortTest):
    def get_sort_algorithm(self):
        return MergeSort()


if __name__ == "__main__":
    unittest.main()
