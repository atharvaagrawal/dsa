""" 
Find the repeating and missing numbers
Problem Statement: You are given a read-only array of N integers with values also in the range [1, N] both inclusive. 
Each integer appears exactly once except A which appears twice and B which is missing. The task is to find the repeating 
and missing numbers A and B where A repeats twice and B is missing.

Example 1:

Input Format:  array[] = {3,1,2,5,3}

Result: {3,4)

Explanation: A = 3 , B = 4 
Since 3 is appearing twice and 4 is missing 
"""
from collections import defaultdict

def find_missing_repeating(l):
    d = defaultdict(lambda:0,{})
    count = 0
    arr = [0 for i in range(len(l)+1)]

    for i in l:
        d[i] += 1
        arr[i] = 1
        if d[i] == 2:
            count = i
    ele = 0
    print(arr)
    for i in range(1,len(arr)):
        if arr[i] == 0:
            ele = i
    print(count,ele)

arr = [3,1,2,5,3]
find_missing_repeating(arr)