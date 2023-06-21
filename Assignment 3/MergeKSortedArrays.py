# uses the technique / data structure of minimum heap
# time complexity - O(nlogk)
# space complexity - O(n)

import math
from Heap import Heap
import heapq


def mergekarrays(k: int, arrays: list) -> list:
    minheap = Heap()
    for i in range(k):
        if len(arrays[i]) > 0:
            minheap.insert((arrays[i][0], i, 0))
    res = []
    while minheap.arr:
        num, array, index = minheap.top()
        minheap.remove()
        res.append(num)
        index += 1
        if index < len(arrays[array]):
            minheap.insert((arrays[array][index], array, index))
    return res
        
assert mergekarrays(2, [[1, 2, 3, 4, 5], [1, 3, 5, 7, 9]]) == [1, 1, 2, 3, 3, 4, 5, 5, 7, 9]
assert mergekarrays( 3, [[1, 4, 7, 9], [2, 6, 7, 10, 11, 13, 15], [3, 8, 12, 13, 16]])== [1, 2, 3, 4, 6, 7, 7, 8, 9, 10, 11, 12, 13, 13, 15, 16]
assert mergekarrays(0, [[]]) == []
assert mergekarrays(0, []) == []
assert mergekarrays(2, [[], []]) == []
assert mergekarrays(2, [[0], []]) == [0]
assert mergekarrays(4, [[-97034, 1, 4], [0, 1, 1201.1231], [9], []]) == [ -97034, 0, 1, 1, 4, 9, 1201.1231]


# took 31 minutes