class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        hashmap = {i:[] for i in range(n)}
        counter = 0
        for e in edges:
            hashmap[e[0]].append(e[1])
            hashmap[e[1]].append(e[0])
        visited = set()
        def dfs(cur):
            visited.add(cur)
            for nei in hashmap[cur]:
                if nei not in visited:
                    dfs(nei)
        for i in range(n):
            if i not in visited:
                counter += 1
                dfs(i)
        return counter
    
        