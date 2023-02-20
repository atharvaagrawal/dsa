# A number N is called a factorial number if it is the factorial of a positive integer. 
# For example, 
# the first few factorial numbers are 1, 2, 6, 24, 120,

""" def factorialNumbers(self, N):
    def findFactorial(n):
    	if n == 1:
    	    return 1
    	res = n * findFactorial(n-1)
        return res
            
    ans = []
        
    while N >= 1:
        t = findFactorial(N)
        if t > N:
            N-=1
        else:
            ans.append(t)
            N-=t
        return ans
 """

def factorialNumbers(N):
        ans = []
        fact = 1
        x = 2
        while fact <= N:
            ans.append(fact)
            fact = fact *x
            x +=1
        return ans

n = int(input("Enter a number:"))

print(factorialNumbers(n))
