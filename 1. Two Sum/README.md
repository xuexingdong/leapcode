# Problem

给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

# Example

```text
给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
```

# Solution

循环两次，穷举计算。

```python
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

```

时间复杂度`n^2`，空间复杂度`1`。

# Optimization

遍历第一遍，记录下各个值对应的下标，第二遍遍历时，根据所需要查的值的情况，到字典中去寻找对应的下标位。

```python
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_map = {}
        for i, num in enumerate(nums):
            idx_map[num] = i
        for i, num in enumerate(nums):
            if target - num in idx_map and idx_map[target - num] != i:
                return [i, idx_map[target - num]]

```

时间复杂度`2n`，空间复杂度`n`。

更进一步，其实一次遍历也可以，不过要注意结果的先后顺序
```python
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_map = {}
        for i, num in enumerate(nums):
            if target - num in idx_map and idx_map[target - num] != i:
                return [idx_map[target - num], i]
            idx_map[num] = i

```