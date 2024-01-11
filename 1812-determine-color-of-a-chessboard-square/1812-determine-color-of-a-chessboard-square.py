class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        if coordinates[0] in ('a','c','e','g') and int(coordinates[1]) in (1,3,5,7):
            return False
        elif coordinates[0] in ('a','c','e','g') and int(coordinates[1]) in (2,4,6,8):
            return True
        elif coordinates[0] in ('b','d','f','h') and int(coordinates[1]) in (1,3,5,7):
            return True
        elif coordinates[0] in ('b','d','f','h') and int(coordinates[1]) in (2,4,6,8):
            return False