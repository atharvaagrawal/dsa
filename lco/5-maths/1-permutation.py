# Permutations Problem
'''
ABC = ABC, ACB, BAC, BCA, CAB, CBA
'''


def permutations(mylist):
    result = []
    permu_helper(mylist, [], result)
    return result


def permu_helper(new_list, temp, result):
    # do all checks
    if len(new_list) == 0:
        temp = ''.join(temp)
        result.append(temp)
        return
    for i in range(len(new_list)):
        permu_helper(new_list[:i]+new_list[i+1:],
                     temp+[new_list[i]], result)


arr = ['A', 'B', 'C', 'D']

print(permutations(arr))
