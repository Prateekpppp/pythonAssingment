# Python program to triple all numbers of a given list of integers. Use Python map.

def triple(n):
    return n+n+n

x = map(triple, [1, 2, 3, 4, 5, 6, 7])

print(list(x))