class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashmap = {i: [] for i in range(numCourses)}
        visited = set()
        cycle = set()
        for crs,pre in prerequisites:
            hashmap[crs].append(pre)
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            cycle.add(crs)
            for pre in hashmap[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visited.add(crs)
        for c in range(numCourses):
            if dfs(c) == False:
                return False
        return True
