class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        hashmap = {i:[] for i in range(n)}
        for i in edges:
            hashmap[i[0]].append(i[1])
            hashmap[i[1]].append(i[0])
        if len(edges) != n-1:
            return False
        visited = set()
        def dfs(cur, prev):
            if cur in visited:
                return False
            visited.add(cur)
            for nei in hashmap[cur]:
                if nei == prev:
                    continue
                if dfs(nei,cur) == False:
                    return False
            return True

        
        return dfs(0,-1) and len(visited) == n