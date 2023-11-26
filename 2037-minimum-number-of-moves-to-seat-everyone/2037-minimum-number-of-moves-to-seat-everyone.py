class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        answer = 0
        sort_seat = sorted(seats)
        sort_student = sorted(students)
        for i in range(len(seats)):
            answer += abs(sort_seat[i] - sort_student[i])
        return answer