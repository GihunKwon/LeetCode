class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        # prices.sort()
        # if prices[0] + prices[1] <= money:
        #     return money - (prices[0] + prices[1])
        # else:
        #     return money

        change = money - sum(sorted(prices)[:2])
        if change >= 0:
            return change
        return money