class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        answer = []
        indices = []
        for i,chr in enumerate(s):
            if chr == c:
                indices.append(i)
        for i in range(len(s)):
            num = float('inf')
            for j in indices:
                num = min(num,abs(i-j))
            answer.append(num)
        return answer