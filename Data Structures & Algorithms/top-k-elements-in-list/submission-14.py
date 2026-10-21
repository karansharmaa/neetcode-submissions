class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = [[] for i in range(len(nums)+1)]
        count = {}
        res = []

        for num in nums: 
            count[num] = count.get(num,0)
        
        for cnt, num in count.items(): 
            freq[num].append(cnt)
        
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == target: 
                    return res 
