class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqs = {i:[] for i in range(numCourses)}

        for cr, pr in prerequisites:
            prereqs[cr].append(pr)

        visit, cycle = set(), set()

        output = []
        def dfs(cr):
            if cr in cycle:
                return False

            if cr in visit:
                return True

            cycle.add(cr)

            for p_cr in prereqs[cr]:
                if not dfs(p_cr): return False

            cycle.remove(cr)
            visit.add(cr)
            output.append(cr)
            return True

        for c in range(numCourses):
            if not dfs(c): return []

        return output

            