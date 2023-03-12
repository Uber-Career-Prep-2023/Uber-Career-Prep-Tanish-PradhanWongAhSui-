# time complexity O(n)
# space complexity O(n)
# hashing technique Hash the elements
# took 8 minutes
# NOTE: It seems like the very nature of the question relies on a very specific input for an accurate
# result to be determined. Hence, the solution below assumes correct input and no edge cases.
def missing_int(n: int, lst : list) -> int:
    my_set = set(lst)
    for i in range(1, n+1):
        if i not in my_set:
            return i

print(missing_int(7, [1, 2, 3, 4, 6, 7]))
# 5
print(missing_int(2, [1]))
# 2
print(missing_int(12, [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12]))
# 9
