import math

def mergekarrays(k: int, arrays: list) -> list:
    # naive solution
    # Time - O(kn) - goes through k number of arrays n times
    # Space - O(n) where n is the total number of elements across all arrays
    indexes = [0] * k
    res = []
    while True:
        array = -1
        min = math.inf
        for i in range(k):
            if indexes[i] < len(arrays[i]) and arrays[i][indexes[i]] < min:
                array = i
                min = arrays[i][indexes[i]]
        if array == -1:
            break
        res.append(min)
        indexes[array] += 1

    return res

# there exists a more efficient solution
# find it

assert mergekarrays(2, [[1, 2, 3, 4, 5], [1, 3, 5, 7, 9]]) == [1, 1, 2, 3, 3, 4, 5, 5, 7, 9]
assert mergekarrays( 3, [[1, 4, 7, 9], [2, 6, 7, 10, 11, 13, 15], [3, 8, 12, 13, 16]])== [1, 2, 3, 4, 6, 7, 7, 8, 9, 10, 11, 12, 13, 13, 15, 16]
assert mergekarrays(0, [[]]) == []
assert mergekarrays(0, []) == []

# took 15 minutes so far