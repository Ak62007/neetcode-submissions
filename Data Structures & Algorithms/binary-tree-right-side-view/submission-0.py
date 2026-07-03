# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        q = collections.deque()
        q.append(root)
        result = []
        while q:
            level_len = len(q)
            nodes = []
            for _ in range(level_len):
                node = q.popleft()
                if node:
                    nodes.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            
            if nodes:
                result.append(nodes[-1])

        return result
