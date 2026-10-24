class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        res = []
        for i, p in enumerate(prices):
            for j, l in enumerate(prices):
                pushed = 0
                if j > i and l <= p:
                    res.append(p - l)
                    pushed = 1
                    break
            if pushed == 0:
                res.append(p)
        return res