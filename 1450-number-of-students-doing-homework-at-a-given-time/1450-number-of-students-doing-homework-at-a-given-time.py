class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        answer = 0
        for i,j in zip(startTime,endTime):
            for k in range(i,j+1):
                if k == queryTime:
                    answer += 1
                    break
        return answer