# Print All Possible Permuation
# https://leetcode.com/problems/permutations/description/

def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def solve(arr,l,r):
            if l == r:
                res.append(arr.copy())
                # print(arr)
            else:
                # 1,2,3
                for i in range(l,r):
                    arr[l], arr[i] = arr[i], arr[l]
                    # print('a',arr)
                    solve(arr, l+1, r)
                    arr[l], arr[i] = arr[i], arr[l]  # backtrack

        solve(nums,0,len(nums))
        return res