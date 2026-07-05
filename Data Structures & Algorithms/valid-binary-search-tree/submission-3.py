# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getMin(self, root):
        if root is None:
            return float('inf')
        return min(root.val, self.getMin(root.left), self.getMin(root.right))

    def getMax(self, root):
        if root is None:
            return float('-inf')

        return max(root.val, self.getMax(root.left), self.getMax(root.right))
           
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        if root.left and root.val <= self.getMax(root.left):
            return False
        if root.right and root.val >= self.getMin(root.right):
            return False

        return self.isValidBST(root.left) and self.isValidBST(root.right)
        