"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def hasSameVals(self, grid) -> bool:
        return all([all(x) for x in grid]) or not any([any(x) for x in grid])
    
    def splitTheGrid(self, grid) -> list[list[list[int]]]:
        l = len(grid[0])
        tl = [row[0:l//2] for row in grid[0:l//2]]
        tr = [row[l//2:l] for row in grid[0:l//2]]
        bl = [row[0:l//2] for row in grid[l//2:l]]
        br = [row[l//2:l] for row in grid[l//2:l]]
        
        return [tl, tr, bl, br]

    def construct(self, grid: List[List[int]]) -> 'Node':
        if self.hasSameVals(grid):
            return Node(grid[0][0], True, None, None, None, None)

        node = Node(1, False, None, None, None, None)
        splits = self.splitTheGrid(grid)
        node.topLeft = self.construct(splits[0])
        node.topRight = self.construct(splits[1])
        node.bottomLeft = self.construct(splits[2])
        node.bottomRight = self.construct(splits[3])

        return node
        