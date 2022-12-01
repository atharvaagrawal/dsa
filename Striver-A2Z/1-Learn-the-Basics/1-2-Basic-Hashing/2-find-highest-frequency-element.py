def mostFrequent(arr):
    d = dict()

    for i in arr:
        if i in d.keys():
            d[i] += 1
        else:
            d[i] = 1

    max_count = 0
    res = -1

    for i in d:
        if max_count < d[i]:
            max_count =  d[i]
            res = i 
    return res 

arr = [10,20,30,20,10,50,10,60,3,10]
print(mostFrequent(arr))