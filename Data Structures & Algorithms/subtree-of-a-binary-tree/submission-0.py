# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check(curr, sub):
            if not curr and not sub:
                return True
            
            if not curr or not sub or curr.val != sub.val:
                return False
            return check(curr.right, sub.right) and check(curr.left, sub.left)
        if not root:
            return False
        return check(root, subRoot) or self.isSubtree(root.left,subRoot) or self.isSubtree(root.right, subRoot)

        