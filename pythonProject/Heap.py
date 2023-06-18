class Heap:
    def __init__(self):

    def top(self) -> int:

    
    def insert(self, x: int):


    def remove(self):



minheap = Heap()
minheap.insert(10)
minheap.insert(0)
minheap.insert(20)
minheap.insert(-1)
minheap.insert(100)
minheap.insert(5)
minheap.insert(1)
minheap.insert(1000)
print(minheap.arr)
while minheap.arr:
    print(minheap.top())
    minheap.remove()
    print(minheap.arr)


