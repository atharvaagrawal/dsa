# Collection in python
# Counter, namedTuple, OrderedDict, defaultdict, deque
from collections import Counter

a = "aaaaabbcc"

my_counter = Counter(a)

print(my_counter.items())
print(my_counter.values())
print(my_counter.most_common(2))


from collections import namedtuple

Point  = namedtuple('Point','x,y')
pt = Point(10,20)
print(pt.x,pt.y)


from collections import OrderedDict

od = OrderedDict()
od['a'] = 1
od['c'] = 2
od['d'] = 3

print(od)


from collections import defaultdict

df = defaultdict(int)
df['a'] = 1
df['c'] = 2

print(df['d'])


from collections import deque
d = deque()

d.append(1)
d.append(2)

d.appendleft(3)

print(d)

d.pop()

print(d)

d.popleft()

print(d)

d.extend([4,5,6])

print(d)

d.rotate(1)

print(d)

d.clear()

print(d)
