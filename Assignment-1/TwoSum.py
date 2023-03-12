# time complexity O(n)
# space complexity O(n)
# Took 15 minutes
# Uses hashing technique
def two_sum(lst: list, k: int)-> int:
    d = {}
    count = 0
    for i in lst:
        if i in d:
            count += d[i]
        d[k-i] = d.get(k-i, 0) + 1
    return count


print(two_sum([1, 10, 8, 3, 2, 5, 7, 2, -2, -1], 10))
# 3
print(two_sum([1, 10, 8, 3, 2, 5, 7, 2, -2, -1], 8))
# 3 (assuming the output specified in the problem description is wrong)
print(two_sum([4, 3, 3, 5, 7, 0, 2, 3, 8, 6], 6))
# 5
print(two_sum([4, 3, 3, 5, 7, 0, 2, 3, 8, 6], 1))
# 0