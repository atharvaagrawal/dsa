# https://practice.geeksforgeeks.org/problems/frequency-of-array-elements-1587115620/0

'''
Given an array A[] of N positive integers which can contain integers from 1 to P where elements can be repeated or can be absent from the array. 
Your task is to count the frequency of all elements from 1 to N.
Note: The elements greater than N in the array can be ignored for counting and do modify the array in-place.


arr[] = {2, 3, 2, 3, 5}
P = 5
Output:
0 2 2 0 1
Explanation: 
Counting frequencies of each array element
We have:
1 occurring 0 times.
2 occurring 2 times.
3 occurring 2 times.
4 occurring 0 times.
5 occurring 1 time.
'''


def frequencyCount(self, arr, N, P):
    my_dict = {}

    for x in arr:
        my_dict[x] = my_dict.get(x, 0) + 1

    # To get the right index even if it doesn't exist. This is a crucial step.
    for i in range(N):
        arr[i] = my_dict[i+1] if i+1 in my_dict else 0

    return arr


# TLE
""" def frequencyCount(arr,P):
        ma = max(arr)
        d = dict()        

        for i in range(1,P+1):
            d[i] = 0
    
        for i in arr:
            d[i] += 1
        
        # print(d)
        arr[0] = d[1]
        ct = 2
        for i in range(1,len(arr)):
            if i not in d.keys() or ct not in d.keys():
                arr[i] = 0
            else:
                arr[i] = d[ct]
            ct+=1
 """
arr = [2, 3, 2, 3, 5]
P = 5

arr = [3, 3, 3, 3]
P = 3

frequencyCount(arr, P)
print("\n Frequency Count:", arr)
