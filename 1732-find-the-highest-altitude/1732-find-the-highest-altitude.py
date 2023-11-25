class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        answer = [0]
        for i in range(len(gain)):
            answer.append(sum(gain[:i+1]))
        return max(answer)