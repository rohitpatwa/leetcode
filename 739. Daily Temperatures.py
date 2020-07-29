# Push (temp, idx) in a stack. Pop element when a bigger elem is seen and update arr[idx] with (new_idx-idx).

# class Solution:
#     def dailyTemperatures(self, T: List[int]) -> List[int]:
#         S = []
#         res = [0]*len(T)
        
#         for i in range(len(T)-1, -1, -1):
#             while S and T[S[-1]] <= T[i]:
#                 S.pop()
#             if S:
#                 res[i] = S[-1] - i
#             S.append(i)
#         return res


class Solution:
    # Time: O(n)
    # Space: O(n)
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0]*len(T)
        stack = []
        for i, t1 in enumerate(T):
            while stack and t1 > stack[-1][1]:
                j, t2 = stack.pop()
                res[j] = i - j
            stack.append((i, t1))
        return res