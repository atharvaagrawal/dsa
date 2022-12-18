# Given a string S(consisting of only lower case characters) and Q queries.
# In each query you are given an integer i and your task is to find the length of longest odd palindromic substring whose middle index is i

def longest_odd_palindromic_substring(s, i):
    left, right = i, i
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    
    print(s[left + 1:right])
    return right - left - 1

s = "aaaaa"
q = [2,3]

# s = "u"
# q = [1,1,1,1,1,1,1,1]

q_set = set(q)

res = [1 for i in range(len(q))]

q_l = list(q_set)
d = dict()

for i in q_l:
    d[i] = longest_odd_palindromic_substring(s, i-1)

for i in range(len(res)):
    res[i] = d[q[i]]

print(res)    