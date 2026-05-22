class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        fmp = 1
        setNum = set(nums)
        for _ in range(len(nums)):
            if fmp in setNum:
                fmp += 1
            else:
                break
        return fmp