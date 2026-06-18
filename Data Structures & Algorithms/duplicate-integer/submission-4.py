class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates = set(nums)
        return len(duplicates) < len(nums)