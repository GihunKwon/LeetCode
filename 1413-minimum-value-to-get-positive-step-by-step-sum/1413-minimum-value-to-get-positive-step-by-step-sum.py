class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        cnt = []
        k = 0
        for i in nums:
            k += i
            cnt.append(k)
        m = min(cnt)

        if m < 0:
            return abs(m) + 1
        else:
            return 1