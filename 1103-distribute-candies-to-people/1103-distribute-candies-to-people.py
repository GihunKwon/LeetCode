class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        answer = [0]*num_people
        candy = 1
        i = 0
        while candies > 0:
            answer[i] += min(candies,candy)
            candies -= candy
            candy += 1
            i = (i+1) % num_people
        return answer
