def pos_sum(a, b):
    out = 0
    carry = 0

    for i in range(32):
        bit1 = (a >> i) & 1
        bit2 = (b >> i) & 1

        if not carry:
            if bit1 and bit2:
                res = 0
                carry = 1
            elif bit1 or bit2:
                res = 1
                carry = 0
            else:
                res = 0
                carry = 0
        else:
            if bit1 and bit2:
                res = 1
                carry = 1
            elif bit1 or bit2:
                res = 0
                carry = 1
            else:
                res = 1
                carry = 0

        out |= res << i

    return out


class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF

        a &= MASK
        b &= MASK

        result = pos_sum(a, b)

        if result <= MAX_INT:
            return result

        return ~(result ^ MASK)