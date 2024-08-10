class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        answer = []
        for i in arr:
            if i == 0:
                answer.append(i)
                answer.append(i)
            else:
                answer.append(i)
        arr[:] = answer[:len(arr)]