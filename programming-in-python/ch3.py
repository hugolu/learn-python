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

################################################################################
# Set

################################################################################
# Map

################################################################################
# iteration
