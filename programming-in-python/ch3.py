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
# Set

s = {7, 'veil', 0, -29, ('x', 11), 'sun', frozenset({8, 4, 7}), 913}
len(s)  # 8

for item in s:
    type(item)

# operations
s = {1, 2, 3}
s.add(3)        # s={1, 2, 3}
s.add(4)        # s={1, 2, 3, 4}
s.clear()       # s=set()

s = {1,2,3}
s.discard(2)    # s={1,3}
s.discard(4)    # s={1,3}
s.remove(3)     # s={1}
#s.remove(4)     # KeyError Exception

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
# Map

################################################################################
# iteration
