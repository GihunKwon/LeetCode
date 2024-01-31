class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split(' ')
        answer = [0] * len(s)
        for i in s:
            answer[int(i[-1])-1] = i[:-1]
        return ' '.join(answer)    
                