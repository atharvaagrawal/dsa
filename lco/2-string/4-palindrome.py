'''
Check if string is palindrome or not

ex: WOW
    Yes it is palindrome

    OLD
    DLO: Not a palindrome
'''

string_input = input('Enter the input String:')


def check_palindrome(original_string):
    reverse_string = []

    for i in range(len(original_string)-1, -1, -1):
        reverse_string.append(original_string[i])

    reverse_string = ''.join(reverse_string)
    if original_string == reverse_string:
        return "It's Palindrome"
    else:
        return "No, It's not Palindrome"


print(check_palindrome(string_input))
