class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        max_ = -1
        for i in range(n-1,-1,-1):
            new_max = max_
            max_ = max(max_,arr[i])
            arr[i] = new_max
        return arr