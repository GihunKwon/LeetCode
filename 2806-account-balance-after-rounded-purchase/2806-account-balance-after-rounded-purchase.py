class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        if purchaseAmount % 10 == 0:
            return 100 - purchaseAmount
        elif purchaseAmount % 5 == 0:
            return 100 - purchaseAmount - 5
        elif 1 <= purchaseAmount % 10 <= 4:
            return 100 - purchaseAmount + (purchaseAmount%10)
        elif 6 <= purchaseAmount % 10 <= 9:
            return 100 - purchaseAmount - (10-(purchaseAmount%10))