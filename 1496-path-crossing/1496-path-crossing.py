class Solution:
    def isPathCrossing(self, path: str) -> bool:
        ans = [[0,0]]
        x,y = 0,0
        for i in path:
            if i == 'S':
                y -= 1
            elif i == 'N':
                y += 1
            elif i == 'E':
                x += 1
            elif i == 'W':
                x -= 1
            if [x,y] in ans:
                return True
            ans.append([x,y])
        return False