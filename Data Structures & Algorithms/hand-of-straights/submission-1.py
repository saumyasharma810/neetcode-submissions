class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize != 0:
            return False
        freq = defaultdict(int)
        hand.sort()
        for num in hand:
            freq[num]+=1
        while freq:
            dict_key = min(freq, key = freq.get)
            for i in range(groupSize):
                if dict_key not in freq:
                    return False
                freq[dict_key]-=1
                if freq[dict_key]==0:
                    del freq[dict_key]
                dict_key+=1
        return True

