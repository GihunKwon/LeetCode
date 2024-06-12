class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        dict = {}
        answer = []
        for i in pieces:
            dict[i[0]] = i
        for j in arr:
            if j in dict:
                answer.extend(dict[j])
        
        return answer == arr