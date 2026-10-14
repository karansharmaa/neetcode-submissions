class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def changes_needed(chunk):
            most = 0 
            for letter in set(chunk):
                most = max(most, chunk.count(letter))
            return len(chunk)-most 
        best = 0 
        for i in range(len(s)):
            for j in range(1, len(s)):
                chunk = s[i:j+1]
                if changes_needed(chunk) <= k: 
                    best = max(best,j-i+1) 
        return best