class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = [[] for i in range(len(nums) + 1)]
        count = {}
        res = []

        #here is where we count the frequencies of each value in nums
        for num in nums: 
            count[num] = 1 + count.get(num, 0)
        
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k: 
                    return res
        return []