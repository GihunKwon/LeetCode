class Solution:
    def fillCups(self, amount: List[int]) -> int:
        answer = 0
        while True:
            if amount == [0]*len(amount):
                return answer
            amount.sort()
            if amount[-1] > 0:
                amount[-1] -= 1
            if amount[-2] > 0:
                amount[-2] -= 1
            answer += 1
        return answer