# Create aux array storing the min_left[i]=min(nums[:i]). Iterate on nums from end and store elements in Stack. In each iteration while S[-1] <= min_left[j]: S.pop().

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        # Strores the ith element from the (i,j,k)
        # min_left[i] = min(nums[:i])
        # min_left will be a non increasing array
        min_left = nums[:]
        for i in range(1, len(nums)):
            min_left[i] = min(min_left[i-1], nums[i-1])

            
        # Stack is meant to store the kth element of (i,j,k)
        # Stack will be a non increasing array
        S = []
        
        for j in range(len(nums)-1, -1, -1): # Iterate in reverse order
            
            # nums[j] is being used for jth element of (i,j,k)
            # nums[j] has to be greater than min_left[j] for it to 
            # make any sense, nums[j] can only be either greater than 
            # min_left[j] or equal to min_left[j]. So we can use '!='
            # operator instead of '>'.
            if nums[j] > min_left[j]: 
                
                # Since stack is holding kth elements, it should be
                # greater than ith element i.e. min_left[j]. So pop
                # all the elements from the stack which are <= 
                # min_left[j].
                while S and S[-1] <= min_left[j]:
                    S.pop()
                
                # If stack has any element left, it means that element is 
                # greater than min_left[j] otherwise it would've been 
                # popped. So now we have (ith element < kth element).
                # We know that the (min_left[j] < nums[j]). 
                # Now we only compare (nums[j] and kth element). 
                
                if S and S[-1] < nums[j]:
                    return True
                
                # If we haven't reached a True condition, keep adding 
                # the element in stack. 
                # S will reamin non-increasing array becaue if any 
                # increasing element shows up, it will become the 
                # desired 132 pattern and return True
                S.append(nums[j])
        return False