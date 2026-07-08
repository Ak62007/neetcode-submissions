class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float('-inf')
        def dfs(root):
            # if root is None:
            #     return (0,0)

            if root.left:
                left_max = dfs(root.left)
            
            if root.right:
                right_max = dfs(root.right)

            if root.left and root.right:
                path_max = max(0, left_max, right_max)
                split_val = root.val + left_max + right_max
                if self.res != max(self.res, root.val + path_max, split_val):
                    self.res = max(self.res, root.val + path_max, split_val)

                return root.val + path_max

            elif root.left or root.right:
                if root.left:
                    path_max = max(0, left_max)
                    
                if root.right:
                    path_max = max(0, right_max)

                if self.res != max(self.res, root.val + path_max):
                    self.res = max(self.res, root.val + path_max)

                return root.val + path_max
            else:
                path_max = 0
                if self.res != max(self.res, root.val + path_max):
                    self.res = max(self.res, root.val + path_max)
                return root.val + path_max

        dfs(root)

        return self.res