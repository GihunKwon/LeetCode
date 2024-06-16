class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common = list(set(list1) & set(list2))
        answer = ['']
        total = float('inf')
        for i in common:
            a = list1.index(i)
            b = list2.index(i)
            if a + b < total:
                total = a+b
                answer = [i]
            elif a + b == total:
                answer.append(i)
        return answer