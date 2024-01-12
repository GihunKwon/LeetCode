class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        answer = [releaseTimes[0]]
        for i in range(1,len(releaseTimes)):
            answer.append(releaseTimes[i] - releaseTimes[i-1])
        
        key = []
        for j,k in zip(answer,keysPressed):
            key.append([j,k])
        return sorted(key,reverse=True)[0][1]
