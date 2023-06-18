# Uses a queue
# time complexity - O(k)
# space complexity - O(k)

from collections import deque

def firstkbnums(k: int)-> list[str]:

    # time - O(k), space - O(k)
    if k < 1:
        return []
    result = ["0"]
    queue = deque(['1'])

    while len(result) < k:
        binary = queue.popleft()
        result.append(binary)

        # using the pattern that consecutive binary numbers follow
        queue.append(binary + '0')
        queue.append(binary + '1')

    return result

assert firstkbnums(5) == ["0", "1", "10", "11", "100"]
assert firstkbnums(10) == ["0", "1", "10", "11", "100", "101", "110", "111", "1000", "1001"]
assert firstkbnums(1) == ["0"]
assert firstkbnums(2) == ["0", "1"]
assert firstkbnums(0) == []
assert firstkbnums(-1) == []

# took 28 minutes 