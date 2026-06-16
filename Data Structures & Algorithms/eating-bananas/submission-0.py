def is_valid(k: int, piles: List[int], h: int) -> bool:
    hrs_took = 0
    for bananas in piles:
        hrs_took += (bananas + k - 1) // k        
   
    if hrs_took > h:
        return False
    else:
        return True


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_k = 1
        max_k = max(piles)
        mid = (min_k + max_k)//2
        min_to_eat = max_k
        while min_k <= max_k:
            # print(f"passing k: {mid}")
            if is_valid(k=mid, piles=piles, h=h):
                max_k = mid - 1
                if mid < min_to_eat:
                    min_to_eat = mid
            else:
                min_k = mid + 1

            mid = (min_k + max_k)//2

        return min_to_eat
