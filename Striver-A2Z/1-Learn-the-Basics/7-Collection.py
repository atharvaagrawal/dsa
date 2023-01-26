# Collection in python
# Counter, namedTuple, OrderedDict, defaultdict, deque
from collections import Counter

a = "aaaaabbcc"

my_counter = Counter(a)

print(my_counter.items())
# dict_items([('a', 5), ('b', 2), ('c', 2)])

print(my_counter.values())
# dict_values([5, 2, 2])

print(my_counter.most_common(2))
# [('a', 5), ('b', 2)]

print(my_counter['d'])
# 0

print(dict(my_counter.most_common(2)),my_counter['a'])
# {'a': 5, 'b': 2} 5

for i in my_counter:
    print(i,my_counter[i])
# a 5
# b 2
# c 2


from collections import namedtuple

Point  = namedtuple('Point','x,y')
pt = Point(10,20)
print(pt.x,pt.y)
# 10 20

from collections import OrderedDict

od = OrderedDict()
od['a'] = 1
od['c'] = 2
od['d'] = 3
print(od)
# OrderedDict([('a', 1), ('c', 2), ('d', 3)])


from collections import defaultdict

df = defaultdict(int)
df['a'] = 1
df['c'] = 2

print(df['d'])
# 0

a = dict()
a = defaultdict(lambda:0,a)
print(a[0])
# 0

print(a[1])
# 0

from collections import deque
d = deque()

d.append(1)
d.append(2)

d.appendleft(3)

print(d)
# deque([3, 1, 2])

d.pop()

print(d)
# deque([3, 1])

d.popleft()

print(d)
# deque([1])

d.extend([4,5,6])

print(d)
# deque([1, 4, 5, 6])

d.rotate(1)

print(d)
# deque([6, 1, 4, 5])

d.clear()

print(d)
# deque([])
