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

# float
s = 3.14.hex()      # '0x1.91eb851eb851fp+1'
f = float.fromhex(s)# 3.14
t = f.hex()         # '0x1.91eb851eb851fp+1'

import math
math.pi * (5 ** 2)  # 78.53981633974483
math.modf(13.732)   # (0.7319999999999993, 13.0)

# complex
3.5+2j              # (3.5+2j)
0.5j                # 0.5j
4+0j                # (4+0j)
-1-3.7j             # (-1-3.7j)

# decimal
import decimal

x = 1.23
y = 3.21
x + y               # 4.4399999999999995

x = decimal.Decimal('1.23')
y = decimal.Decimal('3.21')
x + y               # Decimal('4.44')

################################################################################
# String type

'hello world'       # 'hello world'
"this is a test"    # 'this is a test'
"""first line
second line"""      # 'first line\nsecond line'
""""quote" \n"""    # '"quote" \n'

# compare
a = 'apple'
b = 'banana'

a > b               # False
a >= b              # False
a == b              # False
a != b              # True
a <= b              # True
a < b               # True

# slice
str = '0123456789'

str[3]              # '3'
str[3:7]            # '3456'
str[3:7:2]          # '35'
str[::2]            # '02468'
str[-3]             # '7'
str[-3:-7]          # ''
str[-3:-7:-2]       # '75'
str[::-1]           # '9876543210'

# operation
fruits = ['apple', 'banana', 'cherry']

" ".join(fruits)    # 'apple banana cherry'
"<>".join(fruits)   # 'apple<>banana<>cherry'
"".join(fruits)     # 'applebananacherry'

s = '=' * 5         # '====='
s *= 3              # '==============='

s = 'hello'
s.capitalize()      # 'Hello'
s.center(10, '*')   # '**hello***'
s.count('l')        # 2
s.endswith('lo')    # True
s.endswith('he')    # False
s.find('ll')        # 2
s.index('ll')       # 2
s.isalnum()         # True
s.isalpha()         # True
s.isdigit()         # False
s.islower()         # True
s.ljust(10, '_')    # 'hello_____'
s.rjust(10, '_')    # '_____hello'
s.lower()           # 'hello'
s.replace('e','E')  # 'hEllo'
s.split('l')        # ['he', '', 'o']
s.startswith('lo')  # False
s.stratswith('he')  # True
s.strip('ho')       # 'ell'
s.swapcase()        # 'HELLO'
s.title()           # 'Hello'
s.upper()           # 'Hello'
s.zfill(10)         # '00000hello'

# formating

# variables
"{0} {1}".format(123, "ABC")                # '123 ABC'
"{num} {str}".format(num=123, str="ABC")    # '123 ABC'

# list
list1 = [123, 456]
list2 = ['ABC', 'DEF']
"{0[1]} {1[0]}".format(list1, list2)        # '456 ABC'

# dictionary
d = dict(animal="elepnant", weight=12000)
"The {0[animal]} weights {0[weight]}kg".format(d)   # 'The elepnant weights 12000kg'

# object
"PI={0.pi}".format(math)                    # 'PI=3.14159265359'

# convert
d = decimal.Decimal('3.14')
"{0} {0!s} {0!r}".format(d)                 # "3.14 3.14 Decimal('3.14')"

# formating rules
# { : fill align sign # 0 width, .precision type}
# fill      any char
# align     <, >, ^, =
# sign      force to print '+'
# #         0b, 0o, 0x
# 0         replace space with 0
# width     mininum width
# ,         grouping
# .pre      max length for string, max number after . for floating number
# type      b, c, d, n, o, x, X for int; e, E, f, g, G, n, % for floating

s = "hello"
"#{0:10}#".format(s)    # '#hello     #'
'#{0:>10}#'.format(s)   # '#     hello#'
'#{0:^10}#'.format(s)   # '#  hello   #'

s = "hello world"
maxwidth = 5
"{0}".format(s[:maxwidth])      # 'hello'
"{0:.{1}}".format(s, maxwidth)  # 'hello'

"{0:010}".format(12345)         # '0000012345'
"{0:010}".format(-12345)        # '-000012345'

"{0:*<10}".format(12345)        # '12345*****'
"{0:*>10}".format(12345)        # '*****12345'
"{0:*^10}".format(12345)        # '**12345***'

x = 123
y = -123
"[{0: }] [{1: }]".format(x, y)  # '[ 123] [-123]'
"[{0:+}] [{1:+}]".format(x, y)  # '[+123] [-123]'
"[{0:-}] [{1:-}]".format(x, y)  # '[123] [-123]'

"{0:,}".format(123456789)       # '123,456,789'
"{0:*>13,}".format(123456789)   # '**123,456,789'

r = 5
area = (r ** 2) * math.pi
"[{0:12.2e}]".format(area)      # '[    7.85e+01]'
"[{0:12.2E}]".format(area)      # '[    7.85E+01]'
"[{0:12.2f}]".format(area)      # '[       78.54]'
"[{0:12.2F}]".format(area)      # '[       78.54]'
"[{0:*>12.2e}]".format(area)    # '[****7.85e+01]'
"[{0:*>+12.2e}]".format(area)   # '[***+7.85e+01]'

d = decimal.Decimal(str(math.pi))
"{:,.6f}".format(d)             #  '3.141593'

c1 = 4.75917 + 1.2042j
c2 = 4.75917 - 1.2042j
"{0.real:.3f}{0.imag:+.3f}".format(c1)  # '4.759+1.204'
"{0.real:.3f}{0.imag:+.3f}".format(c2)  # '4.759-1.204'

