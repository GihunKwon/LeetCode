class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        answer = 0
        for i in range(1,len(timeSeries)):
            diff = timeSeries[i] - timeSeries[i-1]
            if diff > duration:
                answer += duration
            else:
                answer += diff
        return answer + duration