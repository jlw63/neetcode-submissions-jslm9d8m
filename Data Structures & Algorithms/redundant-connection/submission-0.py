class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        hashmap = {}
        n = len(edges)

        def dfs(a,b)-> bool:

            if a == b:
                return True
            visited.add(a)
            for neighbours in hashmap[a]:
                if neighbours not in visited:
                    if dfs(neighbours,b):
                        return True
            return False
        for i in range(1,n+1):
            hashmap[i] = []
        for e in edges:
            visited = set()
            if dfs(e[0],e[1]):
                return e
            hashmap[e[0]].append(e[1])
            hashmap[e[1]].append(e[0])