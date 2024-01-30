class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        # answer = 0
        # for i in sentences:
        #     i = i.split(' ')
        #     answer = max(answer,len(i))
        # return answer
        return max(len(i.split(' ')) for i in sentences)