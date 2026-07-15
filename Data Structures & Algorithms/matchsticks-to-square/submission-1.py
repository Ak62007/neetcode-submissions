class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4 != 0:
            return False

        # get the side length
        sl = sum(matchsticks)//4

        cs = [0] * 4

        # sorting
        matchsticks.sort(reverse=True)

        def dfs(i):
            if i == len(matchsticks):
                return True

            for j in range(4):
                if cs[j] + matchsticks[i] <= sl:
                    cs[j] += matchsticks[i]
                    if dfs(i + 1):
                        return True

                    cs[j] -= matchsticks[i]
            return False

        
        return dfs(0)
