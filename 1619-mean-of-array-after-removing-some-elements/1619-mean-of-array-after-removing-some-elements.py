class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        l = int(len(arr) / 100 * 5)
        arr = arr[l:-l]
        return round(sum(arr) / len(arr),5)