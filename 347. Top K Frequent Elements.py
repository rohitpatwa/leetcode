# Linear solution. Create an array of arr to hold all i freq elements at ith arr. Flatten and return last k elements.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq_buckets = [[] for _ in range(len(nums))]
        
        counter = Counter(nums)  
                
        for num, freq in counter.items(): 
            freq_buckets[freq-1].append(num) 
            
        freq_buckets = [x for y in freq_buckets for x in y][::-1]
        return freq_buckets[:k]