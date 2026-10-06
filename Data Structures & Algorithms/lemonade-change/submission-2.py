class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        d_map = {note:0 for note in [5, 10, 20]}
        for bill in bills:
            to_give = bill - 5
            if to_give:
                for note in [10, 5]:
                    denom = to_give // note
                    if denom and d_map[note] >= denom:
                        d_map[note] -= denom
                        to_give -= denom * note
                if to_give == 0:
                    d_map[bill] += 1
                    continue
                else:
                    return False
            else:
                d_map[bill] += 1
        return True