#lower
def low(string):
    return string.lower()
print(low("HELLO WORLD"))

# upper
def upp(string):
    return string.upper()
print(upp("hello world"))

# title
def tit(string):
    return string.title()
print(tit("hello world"))

# capitalize
def ca(string):
    return string.capitalize()
print(ca("hello world"))

# swapcase
def swap(string):
    return string.swapcase()
print(swap("Hello World"))

# islower
def islow(string):
    return string.islower()
print(islow("hello world"))

# isupper
def isupp(string):
    return string.isupper()
print(isupp("HELLO WORLD"))

# istitle
def istit(string):
    return string.istitle()
print(istit("Hello World"))

# isalpha
def isal(string):
    return string.isalpha()
print(isal("HelloWorld"))

# isalnum
def isa(string):
    return string.isalnum()
print(isa("HelloWorld123"))

# isdigit
def isdi(string):
    return string.isdigit()
print(isdi("12345"))

# isspace
def iss(string):
    return string.isspace()
print(iss("   "))


# endswith
def ends(string, suffix):
    return string.endswith(suffix)
print(ends("Hello World", "World"))

# startswith
def st(string, prefix):
    return string.startswith(prefix)
print(st("Hello World", "Hello"))

# count
def co(string, substring):
    return string.count(substring)
print(co("Hello World", "o"))

# find
def f(string, substring):
    return string.find(substring)
print(f("Hello World", "e"))

# strip
def st(string):
    return string.strip()
print(st("   Hello World   "))

# lstrip
def ls(string):
    return string.lstrip()
print(ls("   Hello World   "))

# rstrip
def rs(string):
    return string.rstrip()
print(rs("   Hello World   "))

# split
def sp(string, d):
    return string.split(d)
print(sp("H el lo Wo rl d", " "))

# join
def jo(string, s):
    return s.join(string)
print(jo(["H", "e", "l", "l", "o"], "-"))

# replace
def rep(string, old, new):
    return string.replace(old, new)
print(rep("Hello World", "World", "Python"))

