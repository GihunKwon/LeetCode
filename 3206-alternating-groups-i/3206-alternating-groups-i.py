class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        answer = 0
        colors = colors + colors[:2]
        for i in range(len(colors)-2):
            if colors[i] == colors[i+2] and colors[i] != colors[i+1]:
                answer += 1
        return answer