class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = {}
        for i in hand:
            count[i] = 1 + count.get(i, 0)
        
        hand.sort()
        for num in hand:
            if count[num] != 0:
                for i in range(num, num + groupSize):
                    if i not in count or count[i] <= 0:
                        return False
                    count[i] -= 1
        return True