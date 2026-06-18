class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = collections.defaultdict(list)
        for s in strs: 
            sorteds = ''.join(sorted(s))
            result[sorteds].append(s)
        return list(result.values())