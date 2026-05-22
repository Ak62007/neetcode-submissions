class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapping = defaultdict(int)
        for num in nums:
            mapping[num] += 1

        sorted_items = sorted(mapping.items(), key=lambda item: item[1], reverse=True)
        sorted_dic = dict(sorted_items)
        return list(sorted_dic.keys())[:k]