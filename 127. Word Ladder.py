# Perform bi-directional BFS from start word and end word. Keep track of visited nodes from start and end separately. As you get intersection, return sum of len.

from collections import deque


def adjacent(w1, w2):
    c = 0
    for i in range(len(w1)):
        if w1[i]!=w2[i]:
            c += 1
            if c>1:
                return False
    return True

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        n = len(beginWord)
        
        visited_begin = {beginWord:1}
        Q_begin = deque([(beginWord, 1)])
        
        
        visited_end = {endWord:1}
        Q_end = deque([(endWord, 1)])
        
        
        if n==0 or endWord not in wordList:
            return 0
        
        res = float('inf')
        
        while Q_begin and Q_end:
            
            curr_begin, curr_end = Q_begin.popleft(), Q_end.popleft()
            
            for w in wordList:
                if w not in visited_begin:
                    if adjacent(curr_begin[0], w):
                        if w in visited_end:
                            res = min(res, curr_begin[1] + visited_end[w])
                        Q_begin.append((w, curr_begin[1] + 1))
                        visited_begin[w] = curr_begin[1] + 1

            for w in wordList:
                if w not in visited_end:
                    if adjacent(curr_end[0], w):
                        if w in visited_begin:
                            res = min(res, curr_end[1] + visited_begin[w])
                        Q_end.append((w, curr_end[1] + 1))
                        visited_end[w] = curr_end[1] + 1
            
            if res < float('inf'):
                return res
                    
        return 0