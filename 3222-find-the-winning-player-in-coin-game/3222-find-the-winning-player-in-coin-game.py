class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        y //= 4
        answer = min(x,y)
        if answer % 2 == 1:
            return 'Alice'
        else:
            return 'Bob'