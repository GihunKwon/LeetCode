class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        answer = 0
        for i,j,k in combinations(arr,3):
            if abs(i-j) <= a and abs(j-k) <= b and abs(i-k) <= c:
                answer += 1
        return answer