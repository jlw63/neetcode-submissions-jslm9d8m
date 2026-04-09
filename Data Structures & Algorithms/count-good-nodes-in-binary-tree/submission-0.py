# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, curmax):
            nogood = 0
            if not node:
                return 0
            if node.val >= curmax:
                curmax = node.val
                nogood = 1


            return nogood +dfs(node.left, curmax) + dfs(node.right, curmax)
        return dfs(root, root.val)
        