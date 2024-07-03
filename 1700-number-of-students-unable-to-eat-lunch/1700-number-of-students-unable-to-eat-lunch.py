class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cnt = [0,0]
        for i in students:
            cnt[i] += 1
        
        sand = len(sandwiches)
        for j in sandwiches:
            if cnt[j] == 0:
                break
            if sand == 0:
                break
            cnt[j] -= 1
            sand -= 1
        return sand