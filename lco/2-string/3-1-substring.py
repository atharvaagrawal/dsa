'''
Find out biggest substring without any duplicate:
1) ex: 
   Original String: DADABACERGA
   Substring: BACERG

2) ex: ABBA

3) DVDF

4) PWWKEW

5) anviaj
'''


def longest_substring(string):
    substr = []
    global_max = 0

    #print('len', len(string))
    if len(string) == 0:
        return 0

    if len(string) == 1:
        return 1

    for i in range(len(string)-1):
        check_set = set(string[i])
        j = 0
        flag = 1
        # print('\n\n')
        for j in range(i+1, len(string)):
            #print('i:', i, 'j:', j)
            if string[j] in check_set:
                substr.append(string[i:j])
                flag = 0
                break
            check_set.add(string[j])

        #print('i:', i, 'j:', j)
        #print('le:', len(string[i:j]), 'g:', global_max)

        if flag == 1:
            if (len(string[i:])) >= global_max:
                substr.append(string[i:])
            global_max = max(global_max, (j-i)+1)

        global_max = max(global_max, (j-i))
        # print(string[i:j])

        if(global_max > len(string)/2) and i > len(string)/2:
            break

    largest_arr = 0

    #print('u', len(substr))
    # print(substr)

    lar = 0

    for ele in substr:
        if len(ele) > lar:
            largest_arr = ele
            lar = len(ele)

    return [largest_arr, global_max]


string = input("Enter a String:")
print(longest_substring(string))
