# Data structure design : Add the numbers to dict. In find function, do a linear scan and try to find it's compliment.

class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = defaultdict(int)        

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.s[number] += 1
        

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for n in self.s.keys():
            if ((value - n) in self.s) and (value - n != n or self.s[n] > 1):
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)