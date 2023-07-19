class Heap:
    def __init__(self):
        # time - O(1
        # space - O(1)
        self.arr = []

    def top(self):
        # time - O(1)
        # space - O(1)
        if self.arr:
            return self.arr[0]

    def heapify(self, index):
        # time - O(logn)
        # space - O(logn)
        size = len(self.arr)
        smallest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        if left_child < size and self.arr[left_child] < self.arr[smallest]:
            smallest = left_child
        if right_child < size and self.arr[right_child] < self.arr[smallest]:
            smallest = right_child

        if smallest != index:
            self.arr[smallest], self.arr[index] = self.arr[index], self.arr[smallest]
            self.heapify(smallest)

    def insert(self, x):
        # time - O(logn)
        # space - O(1)
        self.arr.append(x)
        index = len(self.arr) - 1
        while index > 0:
            parent = (index - 1) // 2
            if self.arr[parent] <= self.arr[index]:
                break
            self.arr[parent], self.arr[index] = self.arr[index], self.arr[parent]
            index = parent

    def remove(self):
        # time - O(logn)
        # space - O(1)
        if not self.arr:
            return
        if len(self.arr) == 1:
            self.arr.pop()
            return
        self.arr[0] = self.arr.pop()
        self.heapify(0)

heap = Heap()
heap.insert(4)
heap.insert(2)
heap.insert(7)
assert heap.top() == 2

heap = Heap()
heap.insert(9)
heap.insert(6)
heap.insert(3)
heap.insert(1)
assert heap.top() == 1

heap = Heap()
heap.insert(1)
heap.insert(3)
heap.insert(6)
heap.insert(9)
assert heap.top() == 1

heap = Heap()
heap.insert(5)
heap.insert(3)
heap.insert(8)
heap.insert(2)
heap.remove()
assert heap.top() == 3

heap = Heap()
heap.insert(5)
heap.insert(3)
heap.insert(8)
heap.insert(2)
heap.remove()
heap.remove()
assert heap.top() == 5

heap = Heap()
heap.insert(5)
heap.insert(3)
heap.insert(8)
heap.insert(2)
heap.remove()
heap.remove()
heap.remove()
heap.remove()
assert heap.top() is None

# took about 40 minutes