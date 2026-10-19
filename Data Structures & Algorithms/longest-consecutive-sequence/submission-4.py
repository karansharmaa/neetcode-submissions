class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        best = 0 
        for num in numset: 
            if num-1 not in numset: 
                cur = num 
                length = 1
                while cur + 1 in numset: 
                    cur += 1
                    length += 1
                best = max(best, length)
        return best 
        