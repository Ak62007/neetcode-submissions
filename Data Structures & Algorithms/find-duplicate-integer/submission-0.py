class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        store = {}
        for num in nums:
            if store.get(num, None) is not None:
                return num
            else:
                store[num] = store.get(num, 0) + 1