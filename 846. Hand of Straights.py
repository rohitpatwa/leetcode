# Create a counter of cards. Sort the keys. For each card, next W cards should have a count greater than it's count. Subtract curr count from next W cards.

class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        
        if len(hand)%W != 0:
            return False
        
        counter = {}
        for i in hand:
            counter[i] = counter.get(i, 0) + 1
        
        keys = sorted(counter.keys())
        
        
        for card in keys:
            curr_card_occ = counter[card]
            
            if curr_card_occ == 0:
                continue
            
            for i in range(card, card+W):
                
                if i not in counter:
                    return False
                
                if counter[i] < curr_card_occ:
                    return False
                
                counter[i] -= curr_card_occ
                
        
        return True