class Solution:
    def minChanges(self, n: int, k: int) -> int:
        n = bin(n)[2:]
        k = bin(k)[2:]
        l = max(len(n),len(k))

        n = n.zfill(l)
        k = k.zfill(l)

        answer = 0
        for i,j in zip(n,k):
            if i == '0' and j == '1':
                return -1
            if i == '1' and j == '0':
                answer += 1 
        return answer