class Solution:
    def buildMatrix(self, k: int, rowConditions: list[list[int]], colConditions: list[list[int]]) -> list[list[int]]:
        """
        1. So, my first plan is to run topological sort on two different adj_lists created seperately from rowconditions and colconditions.

        2. Using the both the adj_lists create two valid ordering of one for rows ordering and one for columns.

        3. Now using these two orderings get the indexes of each numbers for the K*K matrix.

        4. Final step initialize the K*K mat and fill the numbers and rest of the numbers would be 0.
        """

        def topological_sort(adj_list) -> list[int]:
            path = set()
            visited = set()

            res = []

            def dfs(node):
                if node in visited:
                    return True

                if node in path:
                    return False

                path.add(node)

                for nei in adj_list[node]:
                    if not dfs(nei):
                        return False

                path.remove(node)
                visited.add(node)
                res.append(node)
                return True

            for key in adj_list:
                if not dfs(key):
                    return []

            return res

        row_adj_list = {i+1:[] for i in range(k)}

        col_adj_list = {i+1:[] for i in range(k)}

        for v1, v2 in rowConditions:
            row_adj_list[v2].append(v1)

        for v1, v2 in colConditions:
            col_adj_list[v2].append(v1)

        row_order = topological_sort(row_adj_list)
        col_order = topological_sort(col_adj_list)

        print(row_order)
        print(col_order)

        if (not row_order) or (not col_order):
            return []

        idx_map = {}

        for i, num in enumerate(row_order):
            idx_map[num] = [i, 0]

        for i, num in enumerate(col_order):
            set_idx = idx_map.get(num, None)
            if set_idx:
                set_idx[1] = i
                idx_map[num] = set_idx
            else:
                idx_map[num] = [0, i]


        ans = [[0]*k for _ in range(k)]

        for key, value in idx_map.items():
            ans[value[0]][value[1]] = key

        return ans