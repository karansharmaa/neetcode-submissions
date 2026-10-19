class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        best = 0 
        for num in nums: 
            cur = num 
            length = 1
            while cur + 1 in nums: 
                cur += 1
                length += 1 
            best = max(best, length)
        return best 
        