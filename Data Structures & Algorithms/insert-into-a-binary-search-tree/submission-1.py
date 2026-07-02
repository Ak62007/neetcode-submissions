# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            new_node = TreeNode(val=val)
            return new_node
        cur = root
        while cur:
            if val > cur.val:
                if cur.right:
                    cur = cur.right
                else:
                    new_node = TreeNode(val=val)
                    cur.right = new_node
                    return root
            else:
                if cur.left:
                    cur = cur.left
                else:
                    new_node = TreeNode(val=val)
                    cur.left = new_node
                    return root
