# this method uses the hashset technique
# time complexity O(n)
# space complexity O(n)
# took 10 minutes
def dedup_array(lst: list)-> list:
    if not lst:
        return []
    j = 0
    for i in range(1, len(lst)):
        if lst[i] != lst[j]:
            j += 1
            lst[j] = lst[i]
    return lst[:j+1]


print(dedup_array([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]))
# [1, 2, 3, 4]
print(dedup_array([0, 0, 1, 4, 5, 5, 5, 8, 9, 9, 10, 11, 15, 15]))
# [0, 1, 4, 5, 8, 9, 10, 11, 15]
print(dedup_array([1, 3, 4, 8, 10, 12]))
# [1, 3, 4, 8, 10, 12]
print(dedup_array([]))
# []