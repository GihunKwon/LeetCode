class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        forward = 0
        backward = 0

        l = len(distance)
        if start > destination:
            start,destination = destination,start

        distance += distance

        for i in range(start,destination):
            forward += distance[i]
        for j in range(destination,l+start):
            backward += distance[j]

        return min(forward,backward)    