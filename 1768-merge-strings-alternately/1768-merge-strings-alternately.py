class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = ''
        for i in range(min(len(word1),len(word2))):
            answer += word1[i]+word2[i]
        diff = max(len(word1),len(word2)) - min(len(word1),len(word2))
        if len(word1) > len(word2):
          answer += word1[-diff:]
        elif len(word1) < len(word2):
          answer += word2[-diff:]
        return answer