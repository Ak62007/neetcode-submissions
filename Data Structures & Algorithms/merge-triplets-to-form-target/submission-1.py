class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        ans = [0, 0, 0]
        for triplet in triplets:
            has = False
            less = True
            for j in range(3):
                if triplet[j] > target[j]:
                    less = False
                    break

                if triplet[j] == target[j]:
                    has = True

            if has and less:
                for i in range(3):
                    ans[i] = max(ans[i], triplet[i])


        if ans == target:
            return True
        else:
            return False