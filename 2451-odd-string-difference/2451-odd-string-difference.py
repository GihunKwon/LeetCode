class Solution:
    def oddString(self, words: List[str]) -> str:
        answer = []
        for i,word in enumerate(words):
            cnt = []
            for j in range(len(word)-1):
                diff = ord(word[j+1]) - ord(word[j])
                cnt.append(diff)
            answer.append(tuple(cnt))
        
        dict = Counter(answer)

        for i in range(len(answer)):
            if dict[answer[i]] == 1:
                return words[i]
