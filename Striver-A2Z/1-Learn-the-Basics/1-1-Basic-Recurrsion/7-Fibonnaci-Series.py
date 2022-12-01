def fib(n):
        # 0,1,1,2,3,5,8,13
        def fibonaci(n):
            if( n == 0):
                return 0
            if( n == 1):
                return 1
            res = fibonaci(n-1) + fibonaci(n-2)
            return res   

        res = fibonaci(n)

        return res

def fibonaci(n,diary={0:0,1:1}):
        if n in diary:
            return diary[n]
        else:
            diary[n] = fibonaci(n-1,diary) + fibonaci(n-2,diary)
            return diary[n]   

print(fib(10))
print(fibonaci(10))