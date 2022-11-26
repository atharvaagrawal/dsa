# Target Triplet
'''
Array: [5,20,12,45,7,15,24,4]
Sum of 3 Element of Array: 34 [15,7,12]
'''

arr = [int(x) for x in input('Enter Array Element: ').split()]
arr.sort()

sum = int(input('Enter Sum Element:'))
print(arr)


def findTargetTriplet(arr, sum, firstEle, thirdEle):

    secondEle = firstEle + 1

    while 1 == 1:
        res = arr[firstEle] + arr[secondEle] + arr[thirdEle]

        print(firstEle, secondEle, thirdEle, res)

        print(res == sum)

        if res == sum:
            print('i')
            return [arr[firstEle], arr[secondEle], arr[thirdEle]]
        elif res < sum:
            secondEle += 1
        elif res > sum:
            thirdEle -= 1

        if thirdEle <= secondEle:
            print('here')
            print("\n")
            firstEle += 1
            secondEle = firstEle + 1
            thirdEle = len(arr) - 1

            if firstEle >= thirdEle or secondEle >= thirdEle:
                print('he')
                return "NO Ele"
            #findTargetTriplet(arr, sum, firstEle, len(arr)-1)


print(findTargetTriplet(arr, sum, 0, len(arr)-1))


'''
def target_triplet(arr, target):
    #assume that array is sorted
    #arr.sort()

    for i in range(len(arr) - 2):

        left = i + 1
        right = len(arr) - 1

        while left < right:
            if(arr[i] + arr[left] + arr[right] == target):
                print("Target location is:" arr[i], ", ", arr[left], "," , arr[right])
                return True #we can also append these values to an existing array

            elif(arr[i] + arr[left] + arr[right] < sum):
                left += 1
            elif(arr[i] + arr[left] + arr[right] > sum):
                right -= 1

    return "NO MATCH"
'''
