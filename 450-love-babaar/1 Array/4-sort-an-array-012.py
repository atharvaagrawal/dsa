# https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1

#User function Template for python3
class Solution:
    def sort012(self,arr,n):
        
        n = len(arr)

        # Traverse through all array elements
        for i in range(n):

            # Last i elements are already in place
            for j in range(0, n-i-1):

                # traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        arr2 = [10,20]
        arr = arr2
        
        for i in  range(len(arr2)):
            arr[i] = arr2[i]
        # count0 = 0
        # count1 = 0
        # count2 = 0
    
        # for i in arr:
        #     if i == 0:
        #         count0 += 1
        #     elif i == 1:
        #         count1 += 1
        #     elif i == 2:
        #         count2 += 1
            
        # arr = list('0'*count0+'1'*count1+'2'*count2) 
        # self.arr = arr
        
        # for i in arr:
        #     print(i,end=' ')
            
        
# Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

 