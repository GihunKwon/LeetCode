class Solution:
    def findLucky(self, arr: List[int]) -> int:
        answer = -1
        for i in set(arr):
            if arr.count(i) == i:
                answer = i
        return answer