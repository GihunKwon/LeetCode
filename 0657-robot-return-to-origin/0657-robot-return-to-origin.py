class Solution:
    def judgeCircle(self, moves: str) -> bool:
        robot = [0,0]
        move = {'U':[-1,0],'D':[1,0],'L':[0,-1],'R':[0,1]}
        for i in moves:
            cur_y,cur_x = robot
            new_y,new_x = move[i]
            robot[0] = cur_y + new_y
            robot[1] = cur_x + new_x
        return robot == [0,0]