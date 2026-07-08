class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float('-inf')
        def dfs(root):
            # if root is None:
            #     return (0,0)

            left_tup = ()
            right_tup = ()
            if root.left:
                left_tup = dfs(root.left)
            
            if root.right:
                right_tup = dfs(root.right)

            if left_tup and right_tup:
                left_wr = left_tup[0]
                left_wor = left_tup[1]
                right_wr = right_tup[0]
                right_wor = right_tup[1]
                left_res = max(root.val + left_wr, root.val + right_wr, root.val)
                right_res = max(left_wr, left_wor, right_wr, right_wor)
                if self.res != max(left_res, right_res, self.res, root.val + left_wr + right_wr):
                    self.res = max(left_res, right_res, self.res, root.val + left_wr + right_wr)

            elif left_tup or right_tup:
                if left_tup:
                    left_wr = left_tup[0]
                    left_wor = left_tup[1]
                    left_res = max(root.val, root.val + left_wr)
                    right_res = max(left_wr, left_wor)
                    
                if right_tup:
                    right_wr = right_tup[0]
                    right_wor = right_tup[1]
                    left_res = max(root.val, root.val + right_wr)
                    right_res = max(right_wr, right_wor)

                if self.res != max(left_res, self.res, right_res):
                    self.res = max(left_res, self.res, right_res)
            else:
                left_res = root.val
                right_res = float('-inf')
                if self.res != max(right_res, self.res, left_res):
                    self.res = max(right_res, self.res, left_res)
            return (left_res, right_res)

        dfs(root)

        return self.res