class Solution:
    def maxTurbulenceSize(self, arr: list[int]) -> int:
        cur = 1
        max_len = float('-inf')
        flag = 'start'
        i = 1
        while i < len(arr):
            if flag == 'start':
                if arr[i-1] > arr[i]:
                    flag = 'true'
                    cur += 1
                elif arr[i-1] < arr[i]:
                    flag = 'false'
                    cur += 1
                else:
                    flag = 'start'
            elif (arr[i] == arr[i-1]):
                flag = 'start'
                max_len = max(max_len, cur)
                cur = 1
            elif (
                (flag == 'true' and arr[i-1] > arr[i])
                or 
                (flag == 'false' and arr[i-1] < arr[i])
                # or 
                # (arr[i] == arr[i-1])
                ):
                max_len = max(max_len, cur)
                cur = 1
                flag = 'start'
                i -= 1
            elif flag == 'true' and arr[i-1] < arr[i]:
                cur += 1
                flag = 'false'
            elif flag == 'false' and arr[i-1] > arr[i]:
                cur += 1
                flag = 'true'
            i += 1

        max_len = max(cur, max_len)
        return max_len
