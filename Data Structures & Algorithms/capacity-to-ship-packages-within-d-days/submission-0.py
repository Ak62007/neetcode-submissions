from collections import deque

def is_valid(capacity: int, weights: List[int], days: int) -> bool:
    weights_dq = deque(weights)
    took_days = 0
    loaded = 0

    while weights_dq:
        if took_days <= days:
            if loaded + weights_dq[0] < capacity:
                item = weights_dq.popleft()
                loaded += item
            elif loaded + weights_dq[0] == capacity:
                weights_dq.popleft()
                took_days += 1
                loaded = 0
            else:
                took_days += 1
                loaded = 0
        else:
            return False


    if loaded > 0:
        took_days += 1

    return took_days <= days


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        min_cap = max(weights)
        max_cap = sum(weights)
        f_min_cap = max_cap

        while min_cap <= max_cap:
            mid_cap = (min_cap + max_cap)//2
            if is_valid(capacity=mid_cap, weights=weights, days=days):
                max_cap = mid_cap - 1
                if mid_cap < f_min_cap:
                    f_min_cap = mid_cap
            else:
                min_cap = mid_cap + 1

        return f_min_cap