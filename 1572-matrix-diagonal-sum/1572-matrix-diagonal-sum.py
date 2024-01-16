class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        # primary = []
        # secondary = []
        # for i in range(len(mat)):
        #     primary.append(mat[i][i])
        # x = len(mat) -1
        # y = 0
        # for j in range(len(mat)):
        #     secondary.append(mat[y][x])
        #     x -=1
        #     y +=1
        # if len(primary) % 2 == 1:
        #     return sum(primary) + sum(secondary) - (primary[len(primary)//2])
        # return sum(primary) + sum(secondary)

        answer = 0
        l = len(mat)
        for i in range(l):
            answer += mat[i][i]
            answer += mat[l-1-i][i]
        if len(mat) % 2 == 1:
            answer -= mat[l//2][l//2]
        return answer