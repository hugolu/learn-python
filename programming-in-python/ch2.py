#!/usr/bin/env python

# Chapter 2 - Data Type

################################################################################
# identifier naming convention
    # don't use python reserved keyword
    # don't name a variable like __VAR__

################################################################################
# Integer type
123     # Int
True    # Bool

# Int Operation
x = 5
y = 3
z = 10

x + y               # 8
x - y               # 2
x * y               # 15
x / y               # 1
x // y              # 1
x % y               # 2
x ** y              # 125
-x                  # -5
+x                  # 5
abs(x)              # 5
divmod(x, y)        # (1, 2)
pow(x, y)           # 125
pow(x, y, z)        # (x**y)%z = 5
round(3.141421, 2)  # 3.14

# Int Convert
i = 1980
s = '0x7bc'
base = 16
x = "1980"

bin(i)              # '0b11110111100'
hex(i)              # '0x7bc'
int(x)              # 1980
int(s, base)        # 1980
oct(i)              # '03674'

# Bit-wise Operation
i = 7
j = 2

i | j               # 7
i ^ j               # 5
i & j               # 2
i << j              # 28
i >> j              # 1
~j                  # -3

# Boolean
t = True
f = False

t and f             # False
f and t             # False
t or f              # True
f or t              # True

################################################################################
# Floating type 

################################################################################
# String type
