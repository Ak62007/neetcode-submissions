class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False
        
        count_map = {}
        for num in hand:
            count_map[num] = count_map.get(num, 0) + 1

        grps = n // groupSize
        for x in sorted(hand):
            if count_map[x]:
                for i in range(x, x + groupSize):
                    if i in count_map and count_map[i]:
                        count_map[i] -= 1
                    else:
                        return False
        return True