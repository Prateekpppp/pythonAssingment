# Python program to square the elements of a list using map() function.


def square(n):
    return n*n

x = map(square, [4, 5, 2, 9])

print(list(x))