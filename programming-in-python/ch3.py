#!/usr/bin/env python

# Chapter 3 - Collections

################################################################################
# Sequence

# tuple
t = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

t[2]                    # 2
t[-3:]                  # (7, 8, 9)
t[:3], "X", t[7:]       # ((0, 1, 2), 'X', (7, 8, 9))
t[:3] + ("X",) + t[7:]  # (0, 1, 2, 'X', 7, 8, 9)

a = 1
b = 2
(a, b) = (b, a)
print(a, b)             # (2, 1)

m = ((1,2,3), (4,5,6), (7,8,9))
m[0][0]                 # 1
m[1][:2]                # (4, 5)

# named tuple
import collections
Sale = collections.namedtuple("Sale", "productid customerid date quantity price")

sales = []
sales.append(Sale(432, 921, "2008-09-14", 3, 7.99))
sales.append(Sale(419, 874, "2008-09-15", 1, 18.49))

total = 0
for sale in sales:
    total += sale.quantity * sale.price

print(total)            # 42.46

# list (mutible)
l = [1, 2, 3, 4, 5]
l.append(3)             # l=[1, 2, 3, 4, 5, 3]
l.count(3)              # 2
l.index(3)              # 2
l.insert(2,2)           # l=[1, 2, 2, 3, 4, 5, 3]
l.pop()                 # l=[1, 2, 2, 3, 4, 5]
l.pop(3)                # l=[1, 2, 2, 4, 5]
l.remove(4)             # l=[1, 2, 2, 5]
l.reverse()             # l=[5, 2, 2, 1]
l.sort()                # l=[1, 2, 2, 5]

total = 0
for i in l:
    total += i          # total=10

total = 0
for i in range(len(l)):
    total += l[i]       # total=10

# list comprehension
nums = []
for num in range(1, 50):
    if (num % 7 == 0 or num % 13 == 0):
        nums.append(num)

nums    # [7, 13, 14, 21, 26, 28, 35, 39, 42, 49]

nums = [n for n in range(1, 50)
        if n % 7 == 0 or n % 13 == 0]

################################################################################
# Set (mutable)

s = {7, 'veil', 0, -29, ('x', 11), 'sun', frozenset({8, 4, 7}), 913}
len(s)  # 8

for item in s:
    type(item)

# operations
s = {1, 2, 3}

len(s)          # 3
2 in s          # True

s.add(3)        # s={1, 2, 3}
s.add(4)        # s={1, 2, 3, 4}
s.clear()       # s=set()

s = {1,2,3}
s.discard(2)    # s={1,3}
s.discard(4)    # s={1,3}
s.remove(3)     # s={1}
#s.remove(4)    # KeyError Exception

s = {1, 2, 3}
s.pop()         # 1
s               # {2, 3}

s = {1, 2, 3}
t = {2, 3, 4}
s.isdisjoint(t) # False
s.issubset(t)   # False
s.issuperset(t) # False

s = {1, 2, 3}
t = {2, 3, 4}
s - t           # {1}           # difference
s & t           # {2, 3}        # intersection
s ^ t           # {1, 4}        # symmetric difference
s | t           # {1, 2, 3, 4}  # union

################################################################################
# Map (mutable)

d1 = {'A': 1, 'B': 2, 'C': 3}   # {'C': 3, 'B': 2, 'A': 1}
d2 = {'B': 2, 'C': 3, 'A': 1}   # {'C': 3, 'B': 2, 'A': 1}

'A' in d1   # True
'D' in d1   # False

# key, value
for item in d1.items():
    print(item[0], item[1])

for key, value in d1.items():
    print(key, value)

for key in d1.keys():
    print(key)

for value in d1.values():
    print(value)

# operations
d1 = {'A': 1, 'B': 2, 'C': 3}   # d1={'A': 1, 'C': 3, 'B': 2}

d2 = d1.copy()                  # d2={'A': 1, 'C': 3, 'B': 2}
d2.clear()                      # d2={}
d2.fromkeys("DEF", 0)           # {'F': 0, 'D': 0, 'E': 0}

d1.get('A')                     # 1
d1.get('D')                     # None
d1.get('D', 0)                  # 0

d1.items()                      # dict_items([('A', 1), ('C', 3), ('B', 2)])
d1.keys()                       # dict_keys(['A', 'C', 'B'])
d1.values()                     # dict_values([1, 3, 2])

d1.pop('A')                     # 1
d1                              # {'C': 3, 'B': 2}
#d1.pop('D')                    # KeyError Exception
d1.pop('D', 0)                  # 0

d1.popitem()                    # ('C', 3)
d1                              # {'B': 2}
d1.setdefault('D', 0)           # 0
d1                              # {'D': 0, 'B': 2}

d1 = {'A': 1, 'B': 2, 'C': 3}
d2 = {'B': 2, 'C': 4, 'D': 4}
d1.update(d2)
d1                              #  {'A': 1, 'C': 4, 'D': 4, 'B': 2}

d1 = {'A': 1, 'B': 2, 'C': 3}
d2 = {'B': 2, 'C': 4, 'D': 4}
d1.items() & d2.items()         # {('B', 2)}
d1.items() | d2.items()         # {('A', 1), ('C', 4), ('D', 4), ('C', 3), ('B', 2)}
d1.items() - d2.items()         # {('A', 1), ('C', 3)}
d1.items() ^ d2.items()         # {('A', 1), ('D', 4), ('C', 3), ('C', 4)}

# ordered dictionary
d = collections.OrderedDict([('z', -1), ('e', -19), ('k', 17)])
d
################################################################################
# iteration

nums = [1, 2, 3, 4, 5]
sum = 0
for n in nums:
    sum += n

print(sum)      # 15

# operations
s = [1, 2, 3]
t = [4 ,5, 6]

s + t           # [1, 2, 3, 4, 5, 6]
s * 3           # [1, 2, 3, 1, 2, 3, 1, 2, 3]

2 in s          # True
2 in t          # False

all(s)          # True
any(s)          # True
s.append(0)     # s=[1, 2, 3, 0]
all(s)          # False
any(s)          # True

len(s)          # 4
max(s)          # 3
min(s)          # 0

s = list(range(1, 10, 3)) # s=[1, 4, 7]
for i in reversed(s):
    print(i)

