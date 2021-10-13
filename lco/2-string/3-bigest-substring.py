'''
Find the length of biggest substring without any duplicate:
ex: 
   Original String: DADABACERGA
   Substring: BACERG
   Output: 6
'''

string_input = input("Enter the String:")


def biggest_substring(string):
    starting_point = 0
    pointer = 0
    global_max = 0
    key_value = {}

    for char in string:
        #print(char, key_value)
        if char in key_value:
            starting_point = max(starting_point, key_value[char]+1)
        #print(starting_point, pointer, global_max, '\n')
        key_value[char] = pointer
        global_max = max(global_max, (pointer-starting_point)+1)
        pointer += 1
    # print(string[starting_point:starting_point+global_max+1])
    return global_max


print(biggest_substring(string_input))
