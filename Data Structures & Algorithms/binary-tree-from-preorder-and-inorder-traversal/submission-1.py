# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def createPreOrder(self, root):
        data = ''
        if root is None:
            return data
        
        data += str(root.val)
        if self.createPreOrder(root.left):
            data += self.createPreOrder(root.left)
        if self.createPreOrder(root.right):
            data += self.createPreOrder(root.right)

        return data

    def createInOrder(self, root):
        data = ''
        if root is None:
            return data

        left = self.createInOrder(root.left)
        if left:
            data += self.createInOrder(root.left)

        data += str(root.val)

        right = self.createInOrder(root.right)
        if right:
            data += self.createInOrder(root.right)

        return data

    def buildTree(self, pre_order, in_order):
        if not pre_order or not in_order:
            return None

        root = TreeNode(pre_order[0])
        mid = in_order.index(pre_order[0])

        root.left = self.buildTree(pre_order[1:mid+1], in_order[0:mid])
        root.right = self.buildTree(pre_order[mid+1:], in_order[mid+1:])

        return root


    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        preorder_str = self.createPreOrder(root)
        inorder_str = self.createInOrder(root)

        data = preorder_str + "_" + inorder_str
        return data
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split("_")
        pre_order = []
        in_order = []
        i = 0
        while i < len(data[0]):
            if data[0][i] == "-":
                pre_order.append(int(f"-{data[0][i+1]}"))
                i += 2
            else:
                pre_order.append(int(data[0][i]))
                i += 1

        i = 0
        while i < len(data[1]):
            if data[1][i] == "-":
                in_order.append(int(f"-{data[1][i+1]}"))
                i += 2
            else:
                in_order.append(int(data[1][i]))
                i += 1

        print(pre_order)
        print(in_order)
        return self.buildTree(pre_order, in_order)
