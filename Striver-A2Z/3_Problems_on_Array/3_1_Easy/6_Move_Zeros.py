# https://leetcode.com/problems/move-zeroes/description/    

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

def moveZeroes(arr):
        """
        Do not return anything, modify nums in-place instead.
        """
        read = 0
        write = 0
        ele = 0

        for i in range(len(arr)):
            if(arr[read] == ele):
                read += 1
            elif(arr[read] != ele):
                arr[write] = arr[read]
                write += 1
                read += 1

        # print('read', read, 'write', write)
        
        if read > 0:
            while write != len(arr):
                arr[write] = ele
                write += 1
        
        return arr