class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        time = arrivalTime + delayedTime
        return time if time < 24 else time- 24