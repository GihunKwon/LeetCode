class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        key = 0
        for i in range(1,10000):
            if i not in arr:
                key += 1
            if key == k:
                return i