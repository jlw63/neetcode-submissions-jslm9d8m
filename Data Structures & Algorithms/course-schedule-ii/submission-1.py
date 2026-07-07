class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hashmap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            hashmap[crs].append(pre)
        cycle = set()
        visit = set()
        result = []
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            cycle.add(crs)
            for pre in hashmap[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            result.append(crs)
            return True
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return result
                

        