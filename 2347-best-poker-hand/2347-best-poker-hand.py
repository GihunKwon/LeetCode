class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1:
            return 'Flush'
        answer = 'High Card'
        for i in set(ranks):
            if ranks.count(i) >= 3:
                answer = 'Three of a Kind'
            elif ranks.count(i) == 2:
                if answer != 'Three of a Kind':
                    answer = 'Pair'
        return answer