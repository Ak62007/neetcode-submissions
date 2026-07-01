# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, right=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is not None:
            return False
        elif q is None and p is not None:
            return False
        elif p is None and q is None:
            return True
            
        self.same = True
        def dfs(p, q):
            if self.same:
                if p.val != q.val:
                    self.same = False
            
            
            if p.left and q.left:
                dfs(p.left, q.left)
            elif ((p.left is None) and (q.left is not None)) or ((p.left is not None) and (q.left is None)):
                self.same = False

            if p.right and q.right:
                dfs(p.right, q.right)
            elif ((p.right is None) and (q.right is not None)) or ((p.right is not None) and (q.right is None)):
                self.same = False

        dfs(p,q)

        return self.same

        
