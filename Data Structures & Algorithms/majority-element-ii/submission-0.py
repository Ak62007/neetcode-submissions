class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mapping = defaultdict(int)
        fa = []
        occ = len(nums)//3
        for num in nums:
            mapping[num] += 1
            if mapping[num] > occ:
                fa.append(num)
        return list(set(fa))