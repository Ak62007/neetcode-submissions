class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        t_of_t = []
        # positions = [False for _ in range(3)]
        for triplet in triplets:
            has = False
            less = True
            for j in range(3):
                if triplet[j] > target[j]:
                    less = False
                    break

                if triplet[j] == target[j]:
                    # positions[j] = True
                    has = True

            if has and less:
                t_of_t.append(triplet)

        print(t_of_t)

        # if not all(positions):
        #     return False

        ans = [0, 0, 0]
        for tr in t_of_t:
            for i in range(3):
                ans[i] = max(ans[i], tr[i])

        if ans == target:
            return True
        else:
            return False