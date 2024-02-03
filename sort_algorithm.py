from abc import ABC, abstractmethod
from typing import List


class SortAlgorithm(ABC):
    @abstractmethod
    def sort(self, nums: List[int]) -> List[int]:
        raise NotImplementedError
