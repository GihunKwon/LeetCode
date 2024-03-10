class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        departure = []
        for path in paths:
            departure.append(path[0])
        for path in paths:
            if path[1] not in departure:
                return path[1]
