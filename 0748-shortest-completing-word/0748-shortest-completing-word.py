class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        answer = ''
        word = defaultdict(int)
        for i in licensePlate:
            if i.isalpha():
                i = i.lower()
                word[i] += 1
        for j in words:
            for alpha,cnt in word.items():
                if j.count(alpha) < cnt:
                    break
            else:
                if not answer:
                    answer = j
                else:
                    if len(answer) > len(j):
                        answer = j
        return answer