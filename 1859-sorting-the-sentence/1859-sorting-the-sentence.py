class Solution:
    def sortSentence(self, s: str) -> str:
        sent = {}
        answer = []
        for i in s.split():
            sent[int(i[-1])] = i[:-1]
        for j in range(1,len(s.split())+1):
            answer.append(sent[j])
        return ' '.join(answer)