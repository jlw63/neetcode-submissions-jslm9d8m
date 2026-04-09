# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        queue = []
        if not root:
            return result
        queue.append(root)
        while queue:
            currentlevel = []
            currentsize = len(queue)
            for i in range(currentsize):
                node = queue.pop(0)
                currentlevel.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            rightview = currentlevel[-1].val
            result.append(rightview)
        return result
                


        