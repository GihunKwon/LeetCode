class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = "qwertyuiop"
        second = "asdfghjkl"
        third = "zxcvbnm"
        answer = []
        for i in words:
            low_i = i.lower()
            if len(set(low_i)) == len(set(low_i) & set(first)):
                answer.append(i)
            if len(set(low_i)) == len(set(low_i) & set(second)):
                answer.append(i)
            if len(set(low_i)) == len(set(low_i) & set(third)):
                answer.append(i)
        return answer