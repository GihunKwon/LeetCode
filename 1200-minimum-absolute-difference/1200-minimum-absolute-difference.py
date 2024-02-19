class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        answer = []
        diff = 0
        for i in range(len(arr)-1):
            if diff == 0:
                diff = abs(arr[i] - arr[i+1])
                answer.append([arr[i],arr[i+1]])
            else:
                if abs(arr[i] - arr[i+1]) == diff:
                    answer.append([arr[i],arr[i+1]])
                elif abs(arr[i] - arr[i+1]) < diff:
                    answer = []
                    answer.append([arr[i],arr[i+1]])
                    diff = abs(arr[i] - arr[i+1])
        return answer