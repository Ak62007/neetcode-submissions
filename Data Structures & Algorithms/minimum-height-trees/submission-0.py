class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        def height_of_tree(i, prev):
            max_hei = 0
            for node in adj[i]:
                if node == prev:
                    continue
                hei = 1 + height_of_tree(node, i)
                if hei > max_hei:
                    max_hei = hei

            return max_hei

        min_heights = []
        for i in range(n):
            min_heights.append((i, height_of_tree(i, -1)))

        
        min_heights.sort(key=lambda x: x[1])

        min_height = min_heights[0][1]

        final_ans = []

        for ans in min_heights:
            if ans[1] == min_height:
                final_ans.append(ans[0])

        return final_ans
