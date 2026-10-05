class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_values = set()

        for el in nums:
            if el in unique_values:
                return True
            unique_values.add(el)
        
        return False
