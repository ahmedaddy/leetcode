
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        row = 0
        direction = 1
        rows = [[] for _ in range(numRows)]
        for c in s:
            rows[row] += c
            if row == numRows -1:
                direction = -1
            elif row == 0:
                direction = 1
            row += direction
        res = ""
        for r in rows:
            for e in r:
                res += e
        return res
