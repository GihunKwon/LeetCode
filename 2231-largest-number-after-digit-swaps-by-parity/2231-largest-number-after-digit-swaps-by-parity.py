class Solution:
    def largestInteger(self, num: int) -> int:
        num = str(num)
        answer = []
        even = []
        odd = []
        for i in num:
            if int(i) % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        even.sort(reverse=True)
        odd.sort(reverse=True)
        for i in num:
            if int(i) % 2 == 0:
                answer.append(even[0])
                even = even[1:]
            else:
                answer.append(odd[0])
                odd = odd[1:]
        
        return int(''.join(answer))