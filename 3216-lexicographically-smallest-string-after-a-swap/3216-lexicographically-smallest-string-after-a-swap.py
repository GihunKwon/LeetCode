class Solution:
    def getSmallestString(self, s: str) -> str:
        answer = [i for i in s]
        for i in range(len(s)-1):
            a,b = int(answer[i]),int(answer[i+1])
            if a > b and a%2 == b%2:
                answer[i],answer[i+1] = answer[i+1],answer[i]
                break
        return ''.join(answer)