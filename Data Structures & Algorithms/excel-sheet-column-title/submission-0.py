class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ch_map = {key: chr(ord('A') + key - 1) for key in range(1, 27)}
        ch_map[0] = 'Z'
        res = []
        while columnNumber:
            rem = columnNumber % 26
            oye = ch_map[rem]
            res.append(oye)
            columnNumber = columnNumber // 26

            if rem == 0:
                columnNumber -= 1

        return ''.join(res[::-1])