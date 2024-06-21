class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == sorted(prices,reverse=True):
            return 0

        buy = prices[0]
        gain = 0
        for i in prices[1:]:
            if buy > i:
                buy = i
            gain = max(gain,i-buy)
        return gain