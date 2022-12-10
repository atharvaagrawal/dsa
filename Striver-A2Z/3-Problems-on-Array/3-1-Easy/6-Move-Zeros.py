# https://leetcode.com/problems/move-zeroes/description/    
def moveZeroes(self, arr: List[int]) -> None:
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