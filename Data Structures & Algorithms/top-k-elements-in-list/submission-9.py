class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #1 count frequencies 
        count = {}
        for num in nums: 
            count[num] = count.get(num,0)+1
        #2 bucket by frequencies 
        buckets = [[] for _ in range(len(nums)+1)]
        for num,freq in count.items():
            buckets[freq].append(num)
        #3 extract top k frequent values 
        result = []
        for i in range(len(buckets)-1,0,-1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result 