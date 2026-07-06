# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root) -> list[int]:
            if root is None:
                return [0,0]
            
            robbed = [0]*2
            robbed_left = dfs(root.left)
            robbed_right = dfs(root.right)

            # with root
            robbed[0] = root.val + robbed_left[1] + robbed_right[1]
            # without root
            robbed[1] = max(robbed_left) + max(robbed_right)

            return robbed

        robbed = dfs(root)

        return max(robbed)