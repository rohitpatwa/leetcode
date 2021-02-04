# Extract values for each place. Create dictionaries for each case at each place. roman = thou[th] + hund[h] + tens[t] + ones[o].

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        thousands = {'0':'', '1':'M', '2':'MM', '3':'MMM'}
        hundreds = {'0':'', '1':'C','2':'CC','3':'CCC','4':'CD','5':'D','6':'DC','7':'DCC','8':'DCCC','9':'CM'}
        tens = {'0':'', '1':'X', '2':'XX', '3':'XXX', '4':'XL', '5':'L', '6':'LX', '7':'LXX', '8':'LXXX', '9':'XC'}
        ones = {'0':'', '1':'I', '2':'II', '3':'III', '4':'IV', '5':'V', '6':'VI', '7':'VII', '8':'VIII', '9':'IX'}
        
        num = str(num).zfill(4)
        th, h, t, o = num
        roman = thousands[th] + hundreds[h] + tens[t] + ones[o]
        return roman
        