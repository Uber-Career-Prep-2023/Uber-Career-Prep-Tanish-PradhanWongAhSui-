import heapq

# technique - maintain two heaps

# time complexity - O(logn) for each addition
# space complexity - O(n)

class RunningMedian:
    def __init__(self):
        self.min_heap = []  
        self.max_heap = []  

    def add_number(self, num):
        if not self.max_heap or num < -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        while len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        while len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def get_median(self):
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        elif len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return self.min_heap[0]


rm = RunningMedian()
rm.add_number(1)
assert rm.get_median() == 1

rm.add_number(11)
assert rm.get_median() == 6

rm.add_number(4)
assert rm.get_median() == 4

rm.add_number(15)
assert rm.get_median() == 7.5

rm.add_number(12)
assert rm.get_median() == 11

rm = RunningMedian()
rm.add_number(5)
assert rm.get_median() == 5

rm.add_number(2)
assert rm.get_median() == 3.5

rm.add_number(8)
assert rm.get_median() == 5

rm.add_number(20)
assert rm.get_median() == 6.5

rm.add_number(13)
assert rm.get_median() == 8

rm.add_number(3)
assert rm.get_median() == 6.5

rm.add_number(9)
assert rm.get_median() == 8

rm.add_number(4)
assert rm.get_median() == 6.5


# time taken 29 minutes