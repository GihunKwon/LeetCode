class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        if coordinates[0] in ('a','c','e','g') and int(coordinates[1]) % 2 == 1:
            return False
        elif coordinates[0] in ('a','c','e','g') and int(coordinates[1]) % 2 == 0:
            return True
        elif coordinates[0] in ('b','d','f','h') and int(coordinates[1]) % 2 == 1:
            return True
        elif coordinates[0] in ('b','d','f','h') and int(coordinates[1]) % 2 == 0:
            return False