class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        length = len(prices)
        if length == 1: return prices
        for i in range(length):
            for j in range(i+1, length):
                if prices[j] <= prices[i]  and i<j:
                    prices[i] -= prices[j]
                    break

        return prices
                