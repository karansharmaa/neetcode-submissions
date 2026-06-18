class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #step 1: count the frequencies 
        count = {}
        for num in nums: 
            count[num] = count.get(num, 0) + 1
        
        #step 2: bucket by frequency 
        buckets = [[] for _ in range(len(nums)+1)]
        for num, freq in count.items(): 
            buckets[freq].append(num)

        #step 3: read buckets from high to low, grab k elements 
        result = []
        for i in range(len(buckets)-1,0,-1): #read the buckets in descending order
            for num in buckets[i]:
                result.append(num)
                if len(result) == k: 
                    return result        