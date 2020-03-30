from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_map = {}
        for i, num in enumerate(nums):
            if target - num in idx_map and idx_map[target - num] != i:
                return [idx_map[target - num], i]
            idx_map[num] = i
