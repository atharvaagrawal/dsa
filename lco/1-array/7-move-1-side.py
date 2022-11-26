'''
Move to 1 Side

5, 6, 10, 0, 60, 61, 0, 90, 0

Move all 0 to left
'''

arr = [int(x) for x in input('Enter array elements: ').split()]

ele = int(input('Enter Element to Move:'))


def moveArray(arr, ele):
    read = len(arr) - 1
    write = len(arr) - 1

    for i in range(len(arr)):
        if(arr[read] == ele):
            read -= 1
        elif(arr[read] != ele):
            arr[write] = arr[read]
            write -= 1
            read -= 1
    print('read', read, 'write', write)
    if read < 0:
        while write >= 0:
            arr[write] = ele
            write -= 1
    return arr


print(moveArray(arr, ele))

'''
def move_to_one_side(arr):
    if len(arr) < 1:
        return "length issues"

    read_stream = len(arr) - 1
    write_stream = len(arr) - 1

    while(read_stream >= 0):
        if arr[read_stream] != 0:
            arr[write_stream] = arr[read_stream]
            write_stream -= 1

        read_stream -= 1

    while(write_stream >= 0):
        arr[write_stream] = 0
        write_stream -= 1

'''
