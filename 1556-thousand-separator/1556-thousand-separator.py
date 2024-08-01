class Solution:
    def thousandSeparator(self, n: int) -> str:
        n = str(n)
        n = n[::-1]
        answer = []
        
        for i in range(0,len(n),3):
            answer.append(n[i:i+3])
        return '.'.join(answer)[::-1]