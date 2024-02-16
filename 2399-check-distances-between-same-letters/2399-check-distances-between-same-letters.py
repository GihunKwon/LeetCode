class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        for i in s:
            first = s.index(i)
            second = s.index(i,first+1)
            dis = distance[ord(i) - 97]
            
            if second - first -1 != dis:
                return False
        return True