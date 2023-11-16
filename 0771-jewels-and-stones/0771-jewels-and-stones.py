class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        answer = 0
        for i in jewels:
            answer += stones.count(i)
        return answer