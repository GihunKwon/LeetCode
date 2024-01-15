class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        answer = 0
        size = truckSize
        box = sorted(boxTypes, key=lambda x:x[1],reverse=True)
        for i in box:
            if i[0] <= size:
                answer += i[0] * i[1]
                size -= i[0]
            elif i[0] > size and size != 0:
                answer += size * i[1]
                size -= size
            if size == 0:
                break
        return answer