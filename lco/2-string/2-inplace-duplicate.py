'''
Inplace duplicates

Ex:
 Original: DADABACDA
 After Removing Duplicates: DABC
'''
string = input("Enter the String: ")


def inplace_duplicate(string):
    read_stream = 0
    write_stream = 0

    string_list = convert_to_char(string)
    set_ds = set()

    for word in string:

        if word not in set_ds:
            string_list[write_stream] = string_list[read_stream]
            write_stream += 1
            set_ds.add(word)

        read_stream += 1

    s = ''.join(string_list[0:write_stream])

    return s


# Python code to convert string to list character-wise
def convert_to_char(string):
    list1 = []
    list1[:0] = string
    return list1


print(inplace_duplicate(string))
