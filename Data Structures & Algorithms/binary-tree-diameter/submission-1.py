class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_dia = 0

        def dfs(treenode: Optional[TreeNode]):
            if treenode is None:
                return 0

            left = dfs(treenode.left)
            right = dfs(treenode.right)

            self.max_dia = max(self.max_dia, left + right)

            return max(left, right) + 1

        dfs(root)

        return self.max_dia
