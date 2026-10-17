class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        start = max(nums)
        end = sum(nums)

        answer = end

        def canSplit(pos_sum):
            cur_sum = 0
            no_of_splits = 0

            for n in nums:
                cur_sum += n

                if cur_sum > pos_sum:
                    cur_sum = n
                    no_of_splits += 1

            return no_of_splits + 1 <= k


        while start <= end:
            mid = start + ((end - start) // 2)

            if canSplit(mid):
                answer = mid
                end = mid - 1
            else:
                start = mid + 1

        return answer

