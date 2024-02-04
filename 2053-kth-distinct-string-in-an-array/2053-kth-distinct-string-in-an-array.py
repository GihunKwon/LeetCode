class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        num = 0
        for i in arr:
            if arr.count(i) == 1:
                num += 1
            if num == k:
                return i
        return ''