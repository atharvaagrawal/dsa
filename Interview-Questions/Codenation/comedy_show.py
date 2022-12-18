# There are 2XN Comedians and M audience member in a comedy show
# First N Male
# Last N Female

# Each Comedian One Slot allocated randomly

# Comedians: Humor level given by array A and charge by array B

# Audience: Tolorence level given by array C and seriousness by array D

# Gender of Member given by array E  1 = Male and 2 = Female

# A comic of same gender as an audience member will make the member laught if there have been atleact C[i] comics before them of the same gender
# such that their humor level is more than D[i] of that member

# A comic of opposite gender as an audience member will make the member laught if there have been atleact C[i] comics before them of the same gender
# such that their humor level is more than 2*D[i] of that member



# Member laughs if
# If Comedians Same Gender as of audience atleast C[i] humor level and A[i] > C[i]
#  Oposite Gender Comedian atleast C[i] and A[i] > D[i]*2 

# If member laughs then  have to pay B[i] to comedian


a = [20,2,8,17]
b = [16,8,8,6]
c = [1,1]
d = [6,9]
e = [1,2]


def comedy_show(A, B, C, D, E):
    payments = [0] * len(C)
    for i in range(len(C)):
        for j in range(len(A)):
            if E[i] == 1 and j < C[i]:
                continue
            if E[i] == 2 and j < C[i] + len(A) // 2:
                continue
            if E[i] == 1 and A[j] > D[i]:
                payments[i] += B[j]
            elif E[i] == 2 and A[j] > 2 * D[i]:
                payments[i] += B[j]
    return payments

A = [20,2,8,17]
B = [16,8,8,6]
C = [1,1]
D = [6,9]
E = [1,2]

# A = [1, 5, 3, 4, 2]
# B = [10, 20, 30, 40, 50]
# C = [1, 2, 1, 2, 1]
# D = [3, 4, 5, 6, 7]
# E = [1, 2, 1, 2, 1]
print(comedy_show(A, B, C, D, E))  # Output: [10, 0, 30, 0, 50]
