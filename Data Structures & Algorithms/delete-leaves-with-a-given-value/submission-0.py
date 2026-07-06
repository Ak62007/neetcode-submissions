# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkLeafNode(self, root) -> bool:
        if not root.left and not root.right:
            return True
        else:
            return False
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if root is None:
            return None
        # check if it is a leaf node
        # if root.left and self.checkLeafNode(root.left):
        #     if root.left.val == Target:
        #         return None
        #     else:
        #         return root.left
        # if root.right and self.checkLeafNode(root.right):
        #     if root.right.val == Target:
        #         return None
        #     else:
        #         return root.right

        if root.left:
            root.left = self.removeLeafNodes(root.left, target)
        if root.right:
            root.right = self.removeLeafNodes(root.right, target)

        if self.checkLeafNode(root):
            if root.val == target:
                return None
            else:
                return root
        else:
            return root

        

