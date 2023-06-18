class Heap:
    def __init__(self):
        self.arr = []

    def top(self) -> int:
        if self.arr:
            return self.arr[0]
    
    def insert(self, x: int):
        self.arr.append(x)
        index = len(self.arr) - 1
        while index > 0:
            parent = (index -1) // 2
            if self.arr[parent] <= self.arr[index]:
                break
            self.arr[parent], self.arr[index] = self.arr[index], self.arr[parent]
            index = parent

    def remove(self):
        if not self.arr:
            return
        if len(self.arr) == 1:
            self.arr.pop()
            return
        self.arr[0] = self.arr.pop()
        index = 0
        size = len(self.arr)
        smallest = 0
        while True:
            smallest = index
            left_child = 2 * index + 1
            right_child = 2 * index + 2
            if left_child < size and self.arr[left_child] < self.arr[smallest]:
                smallest = left_child
            if right_child < size and self.arr[right_child] < self.arr[smallest]:
                smallest = right_child
            if smallest == index:
                break
            self.arr[smallest], self.arr[index] = self.arr[index], self.arr[smallest]
            index = smallest