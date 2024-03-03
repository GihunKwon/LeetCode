class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split(' ')
        s2 = s2.split(' ')
        dict = Counter(s1+s2)
        answer = []

        for key,value in dict.items():
            if value == 1:
                answer.append(key)
        return answer