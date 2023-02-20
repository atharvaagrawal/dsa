# https://takeuforward.org/data-structure/leaders-in-an-array/
""" 
Given an array, print all the elements which are leaders. A Leader is an element that is 
greater than all of the elements on its right side in the array.

Example 1:
Input:
 arr = [4, 7, 1, 0]
Output:
 7 1 0
Explanation:
 Rightmost element is always a leader. 7 and 1 are greater than the elements in their 
 right side.

Example 2:
Input:
 arr = [10, 22, 12, 3, 0, 6]
Output:
 22 12 6
Explanation:
 6 is a leader. In addition to that, 12 is greater than all the elements in its 
 right side (3, 0, 6), also 22 is greater than 12, 3, 0, 6.
"""

def leader(l):
    m = l[-1]

    print(m)
    
    for i in range(len(l)-2,-1,-1):
        if l[i] >= m:
            print(l[i])
            m = l[i]
    
l = [10,22,12,3,0,6]
l = [4,7,1,0]

leader(l)
