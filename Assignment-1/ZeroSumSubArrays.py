# can't really think of edge cases
# statement is not really ambiguous
# approach used is many fixed size sliding windows with the two pointer technique
# time complexity - O(n*1 + (n-1)*2 + (n-2)*3 + (n-3)*4 ...) = arithmetic series -> O(n^2)
# space complexity - O(1) no additional array used, only variables count and total
# took about 15 minutes

def zero_sum_count(lst: list)-> int:
    #     at first thought, an approach that checks every single possible subarray seems difficult to achieve
# naive approach
    count = 0
    total = 0
    for i in range(1, len(lst)):
        if i > 1:
            total = sum(lst[:i])
        else:
            total = lst[0]
        for j in range(i, len(lst)):
            if total == 0:
                count += 1
            total -= lst[j-i]
            total += lst[i]
        if total == 0:
            count += 1
    if len(lst) > 0 and lst[0] == 0:
        count += 1
    return count


print(zero_sum_count([4, 5, 2, -1, -3, -3, 4, 6, -7]))
# expected - 2
print(zero_sum_count([1, 8, 7, 3, 11, 9]))
# expected - 0
print(zero_sum_count([8, -5, 0, -2, 3, -4]))
# expected - 2 (if the output in the homework description is inaccurate)
print(zero_sum_count([]))
# 0
print(zero_sum_count([0, 0]))
# 3
print(zero_sum_count([0]))
# 1
print(zero_sum_count([0, 0, 0, 0]))
# 10
print(zero_sum_count([]))