class Solution:
    def maxTurbulenceSize(self, arr: list[int]) -> int:
        cur = 1
        max_len = float('-inf')
        flag = 's'
        i = 1
        while i < len(arr):
            if flag == 's':
                if arr[i-1] > arr[i]:
                    flag = 't'
                    cur += 1
                elif arr[i-1] < arr[i]:
                    flag = 'f'
                    cur += 1
                else:
                    flag = 's'
            elif (arr[i] == arr[i-1]):
                flag = 's'
                max_len = max(max_len, cur)
                cur = 1
            elif (
                (flag == 't' and arr[i-1] > arr[i])
                or 
                (flag == 'f' and arr[i-1] < arr[i])
                # or 
                # (arr[i] == arr[i-1])
                ):
                max_len = max(max_len, cur)
                cur = 1
                flag = 's'
                i -= 1
            elif flag == 't' and arr[i-1] < arr[i]:
                cur += 1
                flag = 'f'
            elif flag == 'f' and arr[i-1] > arr[i]:
                cur += 1
                flag = 't'
            i += 1

        max_len = max(cur, max_len)
        return max_len
