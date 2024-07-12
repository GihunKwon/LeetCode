class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        answer = 0
        for i in range(len(word)):
            cnt = set()
            for j in range(i,len(word)):
                if word[j] in 'iaeou':
                    cnt.add(word[j])
                    if len(cnt) >= 5:
                        answer += 1
                else:
                    break
        return answer