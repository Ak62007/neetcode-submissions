class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1
        
        q = deque()
        q.append(('0000', 0))
        visited = set(deadends)

        def children(code):
            res = []
            for i in range(4):
                res.append(code[:i] + str((int(code[i]) + 1) % 10) + code[i+1:])
                res.append(code[:i] + str((int(code[i]) - 1 + 10) % 10) + code[i+1:])

            return res

        while q:
            code, turns = q.popleft()
            if code == target:
                return turns

            for child in children(code):
                if child not in visited:
                    visited.add(child)
                    q.append((child, turns + 1))

        return -1