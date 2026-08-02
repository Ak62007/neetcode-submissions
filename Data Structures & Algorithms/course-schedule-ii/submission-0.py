class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        cr_map = {i: [] for i in range(numCourses)}

        for cr, p_cr in prerequisites:
            cr_map[cr].append(p_cr)

        cr_set = set()
        cr_order = []
        def dfs(cr):
            if cr in cr_set:
                return False

            if cr_map[cr] == []:
                if cr not in cr_order:
                    cr_order.append(cr)
                return True

            cr_set.add(cr)

            for p_cr in cr_map[cr]:
                if not dfs(p_cr): return False

            cr_set.remove(cr)
            cr_map[cr] = []
            if cr not in cr_order:
                cr_order.append(cr)
            return True

        for i in range(numCourses):
            if not dfs(i): return []

        return cr_order