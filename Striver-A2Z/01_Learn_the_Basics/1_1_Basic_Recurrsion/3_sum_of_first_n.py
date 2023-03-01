# https://practice.geeksforgeeks.org/problems/sum-of-first-n-terms5843/1

# Given and integer N. Calculate the sum of series 1^3 + 2^3 + 3^3 + 4^3 + … till N-th term.

# TLE
def sumOfSeries(N):
        if N==0:
            return 0
        
        res = N*N*N
        res +=sumOfSeries(N-1)
    
        return res 


def sumOfSeries_(n):
        n = n*(n+1)//2

        print(n)

        res = n*n

        return res

print(sumOfSeries(10)) #3025
print(sumOfSeries_(10)) #3025
