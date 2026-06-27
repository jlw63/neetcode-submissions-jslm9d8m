class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        hashmap = {}
        count = 0
        visited = set()
        for i in range(n):
            hashmap[i] = []
        for e in edges:
            hashmap[e[0]].append(e[1])
            hashmap[e[1]].append(e[0])
        #dfs
        def dfs(node):
            visited.add(node)
            for neighbour in hashmap[node]:
                if neighbour not in visited:
                    dfs(neighbour)
        
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)
        return count


