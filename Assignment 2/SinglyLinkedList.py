class Node:
    pass


class Node:
    def __init__(self, val: int = None):
        # O(1)
        self.val = val
        self.next = None

    def insertAtFront(self, val: int) -> Node:
        # O(1)
        new = Node(val)
        new.next = self
        return new

    # for debugging purposes
    def print(self):
        # O(n)
        curr = self
        string = ""
        while curr:
            string += str(curr.val) + " -> "
            curr = curr.next
        string += "None"
        print(string)

    def insertAtBack(self, val: int):
        # O(n)
        new = Node(val)
        if not self:
            self = new
            return 
        curr = self
        while curr.next:
            curr = curr.next
        curr.next = new

    def insertAfter(self, val: int, loc: Node):
        # O(n)
        if not loc or not self:
            return
        curr = self
        while curr.val != loc.val:
            curr = curr.next
            if not curr:
                return
        temp = curr.next
        curr.next = Node(val)
        curr.next.next = temp

    def deleteFront(self) -> Node:
        # O(1)
        if not self:
            return None
        return self.next

    def deleteBack(self):
        # O(n)
        if not self or not self.next:
            self = None
            return 
        curr = self
        while curr.next.next:
                curr = curr.next
        curr.next = None

    def deleteNode(self, loc: Node) -> Node:
        # O(n)
        if not self:
            return None
        if self.val == loc.val:
            return self.next
        if not self.next:
            return self
        curr = self
        while curr and curr.next.val != loc.val:
            curr = curr.next
        if curr:
            curr.next = curr.next.next
        return self
    # test this 

    def length(self) -> int:
        # O(n)
        count = 0
        curr = self
        while curr:
            count += 1
            curr = curr.next
        return count

    def reverseIterative(self) -> Node:
        # O(n)
        prev = None
        curr = self
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def reverseRecursive(self) -> Node:
        # O(n)
        curr = self
        def reverseR(prev, curr1: Node) -> Node:
            if not curr1:
                return prev
            temp = curr1.next
            curr1.next = prev
            return reverseR(curr1, temp)
        return reverseR(None, curr)



