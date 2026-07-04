# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0
        def dfs(root, nodes):
            nonlocal result
            if root is None:
                return

            is_good = True

            if nodes:
                for node in nodes:
                    if root.val < node:
                        is_good = False
                        break
                
                if is_good:
                    result += 1
            else:
                result += 1

            new_nodes = nodes.copy()
            new_nodes.append(root.val)
            dfs(root.left, new_nodes)
            dfs(root.right, new_nodes)
            return
        
        dfs(root, [])

        return result
        