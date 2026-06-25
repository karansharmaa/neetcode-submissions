class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []

        seen = defaultdict(int)
        for num in nums1: 
            seen[num] = 1
        
        for num in nums2: 
            if seen[num] == 1: 
                seen[num] = 0
                res.append(num)
        return res