def sortTupleinList(lst):
    sorted_list = sorted(lst, key=lambda x: x[-1])
    return sorted_list

print(sortTupleinList([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))