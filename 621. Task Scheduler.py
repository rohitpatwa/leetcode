# ctr=nums except the 1st one which have max_count. total_idle_slots = (max_count-1)*n; res = max_count+ctr+total_idle_slots; return max(res,len(tasks)).

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        vals = sorted(counter.values(), reverse=True)
        max_count = vals[0]
        
        # ctr =  numbers except the first one which have same count as max_count
        ctr = 0
        for x in vals[1:]: 
            if x==max_count:
                ctr += 1
            else:
                break
            
        # this calculates max idle slots. They can be filed by other tasks
        # but they will have to be there
        total_idle_slots = (max_count-1) * (n)
        
        # max_count becaue we want total intervals(including tasks)
        # ctr because we want overflowing tasks which have max_count
        res = max_count + ctr + total_idle_slots
        return max(res, len(tasks))