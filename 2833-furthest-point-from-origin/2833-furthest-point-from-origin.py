class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        m = abs(moves.count('R') - moves.count('L'))
        n = moves.count('_')
        return m+n