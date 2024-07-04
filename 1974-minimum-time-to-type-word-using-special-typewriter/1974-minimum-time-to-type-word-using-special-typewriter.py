class Solution:
    def minTimeToType(self, word: str) -> int:
        answer = len(word)
        cur = 'a'
        for i in word:
            val = abs(ord(i)-ord(cur))
            answer += min(val,26-val)
            cur = i
        return answer