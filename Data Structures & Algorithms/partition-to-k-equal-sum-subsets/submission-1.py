class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False

        ss = sum(nums) // k

        used = [False] * len(nums)

        nums.sort(reverse=True)

        def dfs(i, k, subsetSum):
            if k == 0:
                return True

            if subsetSum == ss:
                return dfs(0, k-1, 0)

            for j in range(i, len(nums)):
                if used[j] or subsetSum + nums[j] > ss:
                    continue

                used[j] = True
                if dfs(j + 1, k, subsetSum + nums[j]):
                    return True

                used[j] = False

            return False

        return dfs(0, k, 0)
            
