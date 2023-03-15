# Uses the technique two-pointer and specifically the fixed size sliding window
# Time complexity O(kn) where n is the length of the array and k is the input k
# ! CAN BE OPTIMIZED TO O(n) !
# Space complexity is O(1) as the extra space used is constant
# Took 15 minutes and 40 seconds

def max_mean_sub(lst: list, k: int) -> float:
    # assuming that k is less than or equal to the length of the given array
    # edge cases
    # should it return 0 if k is 0?
    # should it return 0 or None if the given array is empty
    if lst == [] or k == 0:
        return 0
    max_mean = 0
    for i in range(len(lst)-k+1):  # [1, 2, 3, 4] k = 2 would loop through with i = 0, 1
        p2 = i+k
        curr_mean = sum(lst[i:p2])/k
        if curr_mean > max_mean:
            max_mean = curr_mean
    return max_mean


print(max_mean_sub([4, 5, -3, 2, 6, 1], 2))  # should print 4.5
print(max_mean_sub([4, 5, -3, 2, 6, 1], 3))  # should print 3
print(max_mean_sub([1, 1, 1, 1, -1, -1, 2, -1, -1], 3))  # should print 1
print(max_mean_sub([1, 1, 1, 1, -1, -1, 2, -1, -1, 6], 5))  # should print 1
print(max_mean_sub([], 12))  # should return 0
print(max_mean_sub([1, 12], 0))  # should return 0
