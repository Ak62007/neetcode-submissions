class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rq = deque([])
        dq = deque([])

        for i in range(len(senate)):
            if senate[i] == 'R':
                rq.append(i)
            else:
                dq.append(i)

        while rq and dq:
            r_idx = rq.popleft()
            d_idx = dq.popleft()

            if r_idx < d_idx:
                rq.append(r_idx + len(senate))
            else:
                dq.append(d_idx + len(senate))

        if rq:
            return 'Radiant'
        else:
            return 'Dire'
