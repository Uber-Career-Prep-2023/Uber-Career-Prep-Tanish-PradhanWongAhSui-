class Node:
    pass

class Node:
    def __init__(self, val: int = None):
        # O(1)
        self.val = val
        self.next = None
        self.prev = None

    def insertAtFront(self, val: int) -> Node:
        # O(1)
        new = Node(val)
        if self:
            self.prev = new
            new.next = self
        return new

    # for debugging purposes
    # def print(self):
    #     curr = self
    #     string = ""
    #     while curr:
    #         string += str(curr.val) + " - "
    #         curr = curr.next
    #     string += "None"
    #     print(string)

    # def print_rev(self):
    #     curr = self
    #     while curr.next:
    #         curr = curr.next
    #     string = ""
    #     while curr:
    #         string += str(curr.val) + " - "
    #         curr = curr.prev
    #     string += "None"
    #     print(string)

    def insertAtBack(self, val: int):
        # O(n)
        new_node = Node(val)
        if not self:
            self = new_node
            return
        curr = self
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr

    def insertAfter(self, val: int, loc: Node):
        # O(n)
        if not (self and loc): # this should work right?
            return
        curr = self
        while curr.val != loc.val:
            curr = curr.next
            if not curr:
                return
        temp = curr.next
        new_node = Node(val)
        curr.next = new_node
        new_node.prev = curr
        new_node.next = temp
        if temp:
            temp.prev = new_node
        # test this

    def deleteFront(self) -> Node:
        # O(1)
        if not self:
            return None
        if self.next:
            self.next.prev = None
        return self.next

    def deleteBack(self):
        # O(n)
        if not self or not self.next:
            self = None
            return
        curr = self
        while curr.next:
                curr = curr.next
        curr.prev.next = None

    def deleteNode(self, loc: Node) -> Node:
        # O(n)
        if not self:
            return None
        if self.val == loc.val:
            if self.next:
                self.next.prev = None
            return self.next
        if not self.next:
            return self
        curr = self
        while curr and curr.val != loc.val:
            curr = curr.next
        if curr:
            curr.prev.next = curr.next
            if curr.next:
                curr.next.prev = curr.prev
        return self

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
            curr.prev = temp
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
            curr1.prev = temp
            return reverseR(curr1, temp)
        return reverseR(self, curr)

# my_node = Node(5)
# new = my_node.insertAtFront(10)
# new.insertAtBack(15)
# new.insertAfter(12, Node(5))
# new.print()
# reversed1 = new.reverseRecursive()
# reversed1.print()
# reversed1.print_rev()




