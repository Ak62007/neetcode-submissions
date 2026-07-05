# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodes = []
        def get_sorted_list(root):
            nonlocal nodes
            if root is None:
                return
            
            get_sorted_list(root.left)
            nodes.append(root.val)
            get_sorted_list(root.right)

            return

        get_sorted_list(root)

        return nodes[k-1]