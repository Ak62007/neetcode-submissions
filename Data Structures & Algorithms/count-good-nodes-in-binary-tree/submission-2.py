# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 1
        def dfs(root, gtn):
            nonlocal result
            if root is None:
                return
            if root.val >= gtn:
                result += 1
                gtn = root.val

            dfs(root.left, gtn)
            dfs(root.right, gtn)
            return
        
        dfs(root.left, root.val)
        dfs(root.right, root.val)

        return result
        