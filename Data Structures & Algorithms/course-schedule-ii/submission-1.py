class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c: [] for c in range(numCourses)}
        res = []
        visited = set()
        cycle = set()

        for crs,pre in prerequisites: 
            prereq[crs].append(pre)

        def dfs (crs):
            if crs in cycle: 
                return False
            if crs in visited: 
                return True 
            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False: 
                    return False 
            cycle.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True 
        
        for c in range(numCourses):
            if not dfs(c): 
                return []

        return res 
