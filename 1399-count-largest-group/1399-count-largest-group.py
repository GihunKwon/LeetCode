class Solution:
    def countLargestGroup(self, n: int) -> int:
        # answer = {}
        # for i in range(1,n+1):
        #     i = sum(map(int,str(i)))
        #     if i not in answer:
        #         answer[i] = 1
        #     else:
        #         answer[i] += 1
        # m = max(answer.values())
        # return sum(1 for i in answer.values() if i == m)

        cnt = Counter()
        for i in range(1,n+1):
            total = 0
            while i:
                total += i%10
                i = i//10
            cnt[total] += 1
        return list(cnt.values()).count(max(cnt.values()))