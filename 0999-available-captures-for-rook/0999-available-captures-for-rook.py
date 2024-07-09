class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        answer = 0
        x,y = 0,0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'R':
                    y = i
                    x = j
        # north
        for i in range(y,-1,-1):
            if board[i][x] == 'p':
                answer += 1
                break
            elif board[i][x] == 'B':
                break
        # south
        for i in range(y,8):
            if board[i][x] == 'p':
                answer += 1
                break
            elif board[i][x] == 'B':
                break
        # west
        for i in range(x,-1,-1):
            if board[y][i] == 'p':
                answer += 1
                break
            elif board[y][i] == 'B':
                break
        # east
        for i in range(x,8):
            if board[y][i] == 'p':
                answer += 1
                break
            elif board[y][i] == 'B':
                break

        return answer