class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        dict = Counter()
        for i in range(lowLimit,highLimit+1):
            i = str(i)
            num = 0
            for j in i:
                num += int(j)
            dict[num] += 1
        return sorted(dict.values())[-1]