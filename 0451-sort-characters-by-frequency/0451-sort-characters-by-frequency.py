class Solution:
    def frequencySort(self, s: str) -> str:
        dict = Counter(s)
        sor = sorted(dict.items(), key=lambda x: x[1],reverse = True)
        answer = ''
        for i,j in sor:
            answer += i*j
        return answer
