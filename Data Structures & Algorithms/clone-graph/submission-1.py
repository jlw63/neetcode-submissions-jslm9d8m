"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        hashmap = {}
    
        def cloneNode(node):
            if node in hashmap:
                return hashmap[node]
            clone = Node(node.val)
            hashmap[node] = clone

            for neighbor in node.neighbors:
                clone_neighbor = cloneNode(neighbor)
                clone.neighbors.append(clone_neighbor)
            return clone
        return cloneNode(node)

        