class PriorityQueue:
    def __init__(self):
        # time - O(1)
        # space - O(1)
        self.arr = []

    def top(self) -> int:
        # time - O(1)
        # space - O(1)
        if self.arr:
            return self.arr[0][0]
    
    def insert(self, x: str, weight: int):
        # time - O(logn)
        # space - O(1)
        self.arr.append((x, weight))
        index = len(self.arr) - 1
        while index > 0:
            parent = (index -1) // 2
            if self.arr[parent][1] >= self.arr[index][1]:
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
        index = 0
        size = len(self.arr)
        largest = 0
        while True:
            largest = index
            left_child = 2 * index + 1
            right_child = 2 * index + 2
            if left_child < size and self.arr[left_child] > self.arr[largest]:
                largest = left_child
            if right_child < size and self.arr[right_child] > self.arr[largest]:
                largest = right_child
            if largest == index:
                break
            self.arr[largest], self.arr[index] = self.arr[index], self.arr[largest]
            index = largest

# took about 10 minutes