# https://leetcode.com/problems/rotate-array/description/
def leftRotate(self, arr, k, n):
        # Your code goes here
        
        if k%n == 0:
            return arr
        
        for i in range(k%n):
            p = arr[0]
            arr.remove(arr[0])
            arr.append(p)
        
        return arr

def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if k%n == 0:
            return 
        
        for i in range(k%n):
            p = nums.pop(n-1)
            # nums.remove(nums[-1])
            nums.insert(0,p)
        
        return