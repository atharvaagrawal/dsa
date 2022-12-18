class Solution:
    def smallestValue(self, n: int) -> int:
        
        def primeFactors(n):
            res = 0
            c = 2
            while(n > 1):

                if(n % c == 0):
                    res += c
                    n = n / c
                else:
                    c = c + 1
            return res
        
        
        r = primeFactors(n)
        # prev = 0
        
        while True:
            if n == r:
                break
                
            n = r
            r = primeFactors(n)
        
        return r