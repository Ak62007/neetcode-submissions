class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        idx = 0
        min_dev = abs(arr[0] - x)

        for i in range(1, len(arr)):
            curr_dev = abs(arr[i]-x)
            if curr_dev < min_dev:
                idx = i
                min_dev = curr_dev
            else:
                continue

        print(idx)

        if idx == 0:
            return arr[:k]
        elif idx == len(arr)-1:
            return arr[-k:]
        else:
            result = [arr[idx]]
            counts = k-1
            i = idx - 1
            j = idx + 1
            while counts != 0:
                if i < 0:
                    result.append(arr[j])
                    j += 1

                elif j >= len(arr):
                    result.insert(0, arr[i])
                    i -= 1

                elif abs(arr[i] - x) <= abs(arr[j] - x):
                    result.insert(0, arr[i])
                    i -= 1

                else:
                    result.append(arr[j])
                    j += 1

                counts -= 1

            return result
                
                    
