'''
String Reverse

ex:
 Original: "I am Good"
 Reverse: "Good am I"
'''

string = input("Enter the String:")


def reverse_string(string):
    arr = string.split(' ')

    print(arr)
    rev_str = ''

    for i in range(len(arr)-1, -1, -1):
        rev_str = rev_str+arr[i]+' '
        print(arr[i])

    return rev_str


print(reverse_string(string))


'''
def rev_str(sentence):
    words = sentence.split(" ")

    #words = ["hello", "world"]

    reverse = ' '.join(reversed(words))

    return reverse
'''
