class Solution:
    def sortString(self, s: str) -> str:
        dict = Counter(s)
        answer = ''
        while any(dict.values()):
            for i in sorted(dict.keys()):
                if dict[i] > 0:
                    answer += i
                    dict[i] -= 1
            for i in sorted(list(dict.keys()))[::-1]:
                if dict[i] > 0:
                    answer += i
                    dict[i] -= 1
        return answer