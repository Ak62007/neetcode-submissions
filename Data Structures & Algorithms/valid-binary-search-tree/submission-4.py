# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isvalid(root, left, right):
            if root is None:
                return True

            if not (root.val > left and root.val < right):
                return False

            return (isvalid(root.left, left, root.val) and
                    isvalid(root.right, root.val, right))

        return isvalid(root, float('-inf'), float('inf'))
        