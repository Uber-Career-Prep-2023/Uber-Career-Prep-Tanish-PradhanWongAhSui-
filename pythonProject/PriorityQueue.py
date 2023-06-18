class PriorityQueue:
    def __init__(self):
        self.arr = []

    def top(self) -> int:
        return self.arr[0][0]

    def insert(self, x: str, weight: int):
        self.arr.append((x, weight))
        index = len(self.arr) - 1
        while index > 0:
            parent = (index - 1) // 2
            if self.arr[parent][1] > self.arr[index][1]:
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
        while True:
            lchild = 2 * index + 1
            rchild = 2 * index + 2
            largest = index
            if lchild < len(self.arr) and self.arr[lchild][1] > self.arr[largest][1]:
                largest = lchild
            if rchild < len(self.arr) and self.arr[rchild][1] > self.arr[largest][1]:
                largest = rchild
            if largest == index:
                break
            self.arr[largest], self.arr[index] = self.arr[index], self.arr[largest]
            index = largest

pq = PriorityQueue()
pq.insert("Tanish", 100)
pq.insert("Gyani", 20)
pq.insert("There", 50)
pq.insert("hi", 10)
pq.insert("there we", 1021)
pq.insert("HELLO", 121)
pq.insert("asf", 200)
pq.insert("asdfasdf", 500)
pq.insert("thher", 50002)
print(pq.arr)
while pq.arr:
    print(pq.top())
    pq.remove()
    print(pq.arr)

