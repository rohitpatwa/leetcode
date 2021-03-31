# Create a list of sets for each city. In each set, add the roads in sorted order. We need to check for max rank and second max rank only.

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        cities = [set() for _ in range(n)]
        
        for c1, c2 in roads:
            c1, c2 = sorted([c1, c2])
            cities[c1].add((c1,c2))
            cities[c2].add((c1,c2))
            
        cities = sorted(cities, key=lambda x:len(x), reverse=True)
        
            
        # case0: when there are only 2 cities
        if n == 2:
            return len(cities[0].union(cities[1]))
            
        # case1: 1 with max, 1 with second max
        if len(cities[0]) > len(cities[1]) > len(cities[2]):
            return len(cities[0].union(cities[1]))
        
        # case2: >2 cities with max degree
        if len(cities[0]) == len(cities[1]):
            max_len = len(cities[0])
            last_city_with_max_len = 0
            while last_city_with_max_len < n and \
                len(cities[last_city_with_max_len]) == max_len:
                last_city_with_max_len += 1
            
            for i in range(last_city_with_max_len):
                for j in range(last_city_with_max_len):
                    if i!=j and len(cities[i].union(cities[j]))==2*max_len:
                        return 2*max_len
            return 2*max_len - 1
        
    
        # case3: 1 city with max deg, >2 cities with 2nd max deg
        max_len = len(cities[1])
        last_city_with_max_len = 1
        
        while last_city_with_max_len < n and \
            len(cities[last_city_with_max_len]) == max_len:
            if len(cities[0].union(cities[last_city_with_max_len])) == \
                len(cities[0]) + max_len:
                return len(cities[0]) + max_len
            last_city_with_max_len += 1
        
        return len(cities[0]) + max_len - 1
        