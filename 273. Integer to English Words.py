# Create a sub function to print 3 digit numners. Use that function to print Billions, Millions, Thousands and Hundreds.

import re

class Solution:
    def numberToWords(self, num: int) -> str:
        
        if num==0:
            return "Zero"
        
        def num2words(num):
            
            t_mapping = {
                2:"Twenty", 3:"Thirty", 4:"Forty", 5:"Fifty", 
                6:"Sixty", 7:"Seventy", 8:"Eighty", 9:"Ninety"
            }
            
            o_mapping = {
                0:"", 1:"One", 2:"Two", 3:"Three", 4:"Four", 
                5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 
                9:"Nine", 10:"Ten", 11:"Eleven", 12:"Twelve", 
                13:"Thirteen", 14:"Fourteen", 15:"Fifteen", 16:"Sixteen", 
                17:"Seventeen", 18:"Eighteen", 19:"Nineteen"
            }
            
            h = num//100
            num = num % 100

            t = num//10
            num = num % 10
            
            o = num
            
            res = ""
            
            if h:
                res = f'{o_mapping[h]} Hundred'
            
            if t:
                if t in t_mapping:
                    res += " " + t_mapping[t] + " " + o_mapping[o]
                else:
                    res += " " + o_mapping[int(f'{t}{o}')]
            else:
                res += " " + o_mapping[o]
            
            return re.sub(r'\s+', ' ', res).strip()                 
            

        b = num//10**9
        num = num % 10**9
        
        m = num//10**6
        num = num % 10**6
        
        th = num//10**3
        num = num % 10**3

        h = num
        
        res = ""
        
        B = num2words(b)
        if B:
            res += f'{B} Billion'
            
        M = num2words(m)
        if M:
            res += f' {M} Million'
            
        TH = num2words(th)
        if TH:
            res += f' {TH} Thousand'
        
        H = num2words(h)
        if H:
            res += f' {H}'
        
        return re.sub(r'\s+', ' ', res).strip()
        