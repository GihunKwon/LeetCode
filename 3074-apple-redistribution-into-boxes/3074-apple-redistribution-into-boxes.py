class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total = sum(apple)
        capacity.sort(reverse=True)
        answer = 0
        cnt = 0
        for i in capacity:
            answer += 1
            cnt += i
            if cnt >= total:
                return answer
        return answer