class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        def dfs(node, parent)->bool:
            visited.add(node)
            for neighbour in hashmap[node]:
                if neighbour not in visited:
                    if dfs(neighbour, node):
                        return True
                elif neighbour != parent:
                    return True
            return False

            
        hashmap = {}
        for i in range(n):
            hashmap[i] = []
        for e in edges:
            hashmap[e[0]].append(e[1])
            hashmap[e[1]].append(e[0])
        cycle = dfs(0,None)
        if cycle or len(visited) != n:
            return False
        return True
