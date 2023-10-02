# Python function to sum all the numbers in a list.

def sumoflist(list):
    sum = 0
    for i in list:
        sum += i
    return sum

print(sumoflist([8, 2, 3, 0, 7]))    
    