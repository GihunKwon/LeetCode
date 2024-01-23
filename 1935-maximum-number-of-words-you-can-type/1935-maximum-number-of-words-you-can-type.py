class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        a = text.split(' ')
        answer = [0]*len(a)
        for i,word in enumerate(a):
            for j in list(brokenLetters):
                if j in word:
                    answer[i] += 1
        return answer.count(0)