# Fibonaci: [0,1,1,2,3,5,8,13]

fibo_n = int(input("Enter the Fibo Number:"))
arr = [0, 1]
f = 1


def fibo(arr, f):

    if f == fibo_n-1:
        return arr

    arr.append(arr[f-1]+arr[f])

    return fibo(arr, f+1)


print(fibo(arr, f))
