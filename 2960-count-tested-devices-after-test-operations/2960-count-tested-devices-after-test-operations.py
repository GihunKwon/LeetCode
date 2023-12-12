class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        for i in range(len(batteryPercentages)):
            for j in range(i+1,len(batteryPercentages)):
                if batteryPercentages[i] > 0:
                    if batteryPercentages[j] > 0 :
                        batteryPercentages[j] -= 1
        return len(batteryPercentages) - batteryPercentages.count(0)