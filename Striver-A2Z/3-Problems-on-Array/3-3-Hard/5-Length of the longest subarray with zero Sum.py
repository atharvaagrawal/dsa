""" 
Given an array containing both positive and negative integers, 
we have to find the length of the  longest subarray with the sum of all elements equal to zero. 

Input Format: N = 6, array[] = {9, -3, 3, -1, 6, -5}
Result: 5
Explanation: The following subarrays sum to zero:
{-3, 3} , {-1, 6, -5}, {-3, 3, -1, 6, -5}
Since we require the length of the longest subarray, our answer is 5!
"""

def longestSubArrayWithSum0(l):
    max_len = 0
    hashmap = dict()
    s = 0

    for i in range(len(l)):
        s += l[i]
        print(s,i)
        if s != 0 and s not in hashmap:
            hashmap[s] = i
            continue
        
        if s == 0:
            max_len = max(max_len,i+1)
        else:
            if s in hashmap:
                max_len = max(max_len,i - hashmap[s])
        
    print("\n\n Max Len with SubArray 0:",max_len)

array = [9,-3,3,-1,6,-5]
# array = [-1,1,-1,1]

longestSubArrayWithSum0(array)

