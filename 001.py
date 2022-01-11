# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

# 你可以按任意顺序返回答案。

# 注：数字有相同的如，[3, 3]且target=6

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map=dict()
        for ind,num in enumerate(nums):
            hash_map[num] = ind
        for i,num in enumerate(nums):
            j = hash_map.get(target - num)
            if j is not None and i!=j:
                return [i,j]