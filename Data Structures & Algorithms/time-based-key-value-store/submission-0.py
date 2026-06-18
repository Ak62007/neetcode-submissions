class TimeMap:

    def __init__(self):
        self.double_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.double_map.get(key, None) is None:
            self.double_map[key] = [(timestamp, value)]
        else:
            self.double_map[key].append((timestamp, value))

        return

    def get(self, key: str, timestamp: int) -> str:
        if self.double_map.get(key, None) is None:
            return ""
        else:
            arr = self.double_map[key]
            l, r = 0, len(arr) - 1
            ans = ""
            while l <= r:
                mid = (l + r)//2
                if arr[mid][0] <= timestamp:
                    l = mid + 1
                    ans = arr[mid][1]
                else:
                    r = mid - 1

            return ans