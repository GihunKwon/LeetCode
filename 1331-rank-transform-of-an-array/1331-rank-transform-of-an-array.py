class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        s = sorted(set(arr))
        dict = {}
        for i in range(len(s)):
            dict[s[i]] = i+1
        for j in range(len(arr)):
            arr[j] = dict[arr[j]]
        return arr