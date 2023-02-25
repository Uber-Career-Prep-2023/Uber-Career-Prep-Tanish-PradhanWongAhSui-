# Given a list of integer pairs representing the low and high end of an interval, inclusive,
# return a list in which overlapping intervals are merged.
# 7 minutes

def merge_intervals(lst: list)-> list:
    lst2 = []
    for i in lst:
        for j in range(i[0], i[1]):
            lst2.append(j)
    lst2 = sorted(lst2)
    for i in range(lst2[0], lst[-1]):
        if i in lst

print(merge_intervals([(2, 3), (4, 8), (1, 2), (5, 7), (9, 12)]))
# [(4, 8), (1, 3), (9, 12)]
print(merge_intervals([(5, 8), (6, 10), (2, 4), (3, 6)]))
# [(2, 10)]
print(merge_intervals([(10, 12), (5, 6), (7, 9), (1, 3)]))
# [(10, 12), (5, 6), (7, 9), (1, 3)]