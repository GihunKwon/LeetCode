class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        answer = []
        for i in image:
            frame = []
            for j in i[::-1]:
                if j == 0:
                    frame.append(1)
                else:
                    frame.append(0)
            answer.append(frame)
        return answer