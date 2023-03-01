# https://leetcode.com/problems/next-permutation/description/

def nextPermutation(num):
    # 1 Linearly traverse from back to front
    ind1 = -1

    for i in range(len(num)-2,-1,-1):
        if num[i] < num[i+1]:
            ind1 = i
            break

    if ind1 == -1:
            num[0:] = num[0:][::-1]
            print(num)
            return 
    # 2 Linearly traverse from back to front and find index greater than ind1
    ind2 = 0
    for i in range(len(num)-1,-1,-1):
        if num[i] > num[ind1]:
            ind2 = i
            break
    
    # 3 Swap ind1 and ind2
    num[ind1],num[ind2] = num[ind2],num[ind1]

    print(num)

    # 4 Reverse the array from ind1+1 to end
    num[ind1+1:] = num[ind1+1:][::-1]

    print(num)

array = [1,3,5,4,2]
array = [1,3,2]

nextPermutation(array)