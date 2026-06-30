# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        self.isbal = True

        def dfs(root):
            if root is None:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            if self.isbal:
                if abs(left - right) > 1:
                    self.isbal = False
            
            return max(left, right) + 1

        dfs(root)

        return self.isbal


        