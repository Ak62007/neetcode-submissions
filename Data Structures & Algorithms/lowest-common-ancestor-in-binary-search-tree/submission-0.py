# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def parentsOfANode(self, root, node) -> list[TreeNode]:
        if root is None:
            return []

        parents = []
        if root.val == node.val:
            parents.append(root)
            return parents

        if root.val > node.val:
            parents.append(root)
            parents.extend(self.parentsOfANode(root.left, node))
        else:
            parents.append(root)
            parents.extend(self.parentsOfANode(root.right, node))

        return parents

        

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_parents = self.parentsOfANode(root, p)
        q_parents = self.parentsOfANode(root, q)

        intsec_pars = [parent for parent in p_parents if parent in set(q_parents)]

        return intsec_pars[-1]
        