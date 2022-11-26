
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

def add2_val(l):
    l.add(10)
    l = tuple(map(lambda x: x+2,l))

l = (1,2,3,4,5)

print("Before Function Call:",l)
add2_val(l)
print("After Function Call:",l)

