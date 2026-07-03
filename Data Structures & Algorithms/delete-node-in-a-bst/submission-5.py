# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root

        if root.val == key:
            if root.left and root.right:
                cur = root.left
                while cur.right:
                    cur = cur.right

                cur.right = root.right
                return root.left
            elif root.left or root.right:
                if root.left:
                    return root.left
                else:
                    return root.right
            else:
                return None


        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)

        return root