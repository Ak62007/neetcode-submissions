class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        cr_map = {i:[] for i in range(numCourses)}
        for cr, pre in prerequisites:
            cr_map[cr].append(pre)

        cr_set = set()

        def dfs(cr):
            if cr in cr_set:
                return False

            if cr_map[cr] == []:
                return True

            cr_set.add(cr)

            for p_cr in cr_map[cr]:
                if not dfs(p_cr): return False

            cr_set.remove(cr)
            cr_map[cr] = []
            return True

        for i in range(numCourses):
            if not dfs(i): return False

        return True