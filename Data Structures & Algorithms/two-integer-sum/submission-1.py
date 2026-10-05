class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for el in nums:
            potential_target = 0
            for i in range(nums.index(el), len(nums)):
                potential_target = el + nums[i]
                if target == potential_target and nums.index(el) != i:
                    return [nums.index(el), i]

