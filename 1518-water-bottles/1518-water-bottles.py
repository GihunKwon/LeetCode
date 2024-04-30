class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        answer = numBottles

        while True:
            answer += numBottles // numExchange

            numBottles = numBottles//numExchange + numBottles%numExchange
        
            if numBottles < numExchange:
                break

        return answer