# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        checkup = {v:i for i,v in enumerate(inorder)}

        n = len(preorder)
        p = deque(preorder)

        def rec(start, end):
            if start > end:
                return None
            else:
                cand = p.popleft()
                root = TreeNode(cand)
                mid = checkup[cand]
                root.left = rec(start,mid-1)
                root.right = rec(mid+1,end)
                return root
        return rec(0,n-1)

