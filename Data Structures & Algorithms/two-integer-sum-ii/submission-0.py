class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans = []
        i = 0
        j = len(numbers) - 1
        while(True):
            if numbers[i] + numbers[j] == target:
                ans.append(i)
                ans.append(j)
                break
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                j -= 1

        ans[0] = numbers.index(numbers[ans[0]]) + 1
        ans[1] = numbers.index(numbers[ans[1]]) + 1

        return ans