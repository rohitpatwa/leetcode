# Maintin the distance from origin on x axis and y axis.

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x, y = 0, 0
        for i in moves:
            if i=='L':
                x -= 1
            elif i == 'R':
                x += 1
            elif i == 'U':
                y += 1
            else:
                y -= 1
                
        if x==0 and y==0:
            return True
        return False