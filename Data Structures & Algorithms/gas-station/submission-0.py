class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total = 0
        ans_idx = 0
        n = len(gas)

        for i in range(n):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                ans_idx = i+1

        return ans_idx
                