class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num = ''.join(str(ord(i)-96) for i in s)
        
        for _ in range(k):
            num = str(sum(int(i) for i in num))

        return int(num)