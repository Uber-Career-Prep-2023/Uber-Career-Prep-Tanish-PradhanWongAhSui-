# uses the technique of sorting and then solving
# space complexity is O(1) not counting the input or output
# time complexity is O(nlogn) because sort function
# 25 minutes

def merge_intervals(lst: list)-> list:
    if not lst:
        return []
    if not lst[0]:
        return [[]]
    res = []
    lst.sort(key=lambda x: x[0])
    print(lst)
    curr = lst[0]
    res.append(curr)
    for i in range(1, len(lst)):
        curr = lst[i]
        if curr[0] > res[-1][1]:
            res.append(curr)
        elif curr[0] <= res[-1][1] and curr[1] > res[-1][1]:
            res[-1][1] = curr[1]
    return res

print(merge_intervals([[2, 3], [4, 8], [1, 2], [5, 7], [9, 12]]))
# [[4, 8], [1, 3], [9, 12]]
print(merge_intervals([[5, 8], [6, 10], [2, 4], [3, 6]]))
# [(2, 10)]
print(merge_intervals([[10, 12], [5, 6], [7, 9], [1, 3]]))
# [(10, 12), (5, 6), (7, 9), (1, 3)]
print(merge_intervals([]))
print(merge_intervals([[]]))