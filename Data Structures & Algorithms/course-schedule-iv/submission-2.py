class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        if not prerequisites:
            return [False for i in range(len(queries))]
        adjList = {i:[] for i in range(numCourses)}

        for pr, cr in prerequisites:
            adjList[cr].append(pr)
        
        def dfs(cr):
            if cr not in prereqMap:
                prereqMap[cr] = set()
                for prereq in adjList[cr]:
                    prereqMap[cr] |= dfs(prereq)

                prereqMap[cr].add(cr)
            return prereqMap[cr]

        prereqMap = {}
        for i in range(numCourses):
            dfs(i)

        res = []
        for u, v in queries:
            res.append(u in prereqMap[v])

        return res