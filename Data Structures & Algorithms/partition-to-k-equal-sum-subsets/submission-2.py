class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k:
            return False

        target = total // k
        nums.sort(reverse=True)

        if nums[0] > target:
            return False

        used = [False] * len(nums)

        def dfs(start, k, curr):
            if k == 1:
                return True

            if curr == target:
                return dfs(0, k - 1, 0)

            for j in range(start, len(nums)):
                if used[j]:
                    continue

                if curr + nums[j] > target:
                    continue

                if j > start and nums[j] == nums[j - 1] and not used[j - 1]:
                    continue

                used[j] = True

                if dfs(j + 1, k, curr + nums[j]):
                    return True

                used[j] = False

                # Symmetry pruning
                if curr == 0:
                    break

            return False

        return dfs(0, k, 0)