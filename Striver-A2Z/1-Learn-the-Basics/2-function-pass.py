
# In Python there are mutable and immutable object

# Pass By Value
# Immutable: int,float,long,complex,string,tuple,bool

# Pass By Reference
# Mutable: list, dict, set, byte, array, userdefined classes


# Pass By Reference
def add2_ref(l):
    print(id(l))
    l.append(6)
    print(id(l))
    l = list(map(lambda x: x+2,l))
    print(id(l))
    
l = [1,2,3,4,5]
print(id(l))
print("Before Function Call:",l)
add2_ref(l)
print("After Function Call:",l)

# 139734178810304
# Before Function Call: [1, 2, 3, 4, 5]
# 139734178810304
# 139734178810304
# 139734177013440
# After Function Call: [1, 2, 3, 4, 5, 6]


def add2_val(l):
    l.add(10)
    l = tuple(map(lambda x: x+2,l))

l = (1,2,3,4,5)

print("Before Function Call:",l)
add2_val(l)
print("After Function Call:",l)

# Before Function Call: (1, 2, 3, 4, 5)
# Traceback (most recent call last):
#   File "/media/atharva/Study/dsa/Striver-A2Z/1-Learn-the-Basics/2-function-pass.py", line 32, in <module>
#     add2_val(l)
#   File "/media/atharva/Study/dsa/Striver-A2Z/1-Learn-the-Basics/2-function-pass.py", line 26, in add2_val
#     l.add(10)
# AttributeError: 'tuple' object has no attribute 'add'