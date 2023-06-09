# remove duplicates for unsorted and sorted linked list

#  1 -> 3 -> 5 -> 3
class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None

    def print(self):
        curr = self
        toprint = ""
        while curr:
            toprint += str(curr.val)
            toprint += " -> "
            curr = curr.next
        toprint += "None"
        print(toprint)

def removeD(head: Node):
    # unsorted
    # Time - O(n)
    # Space - O(n)
    if not head:
        return 
    seen = set()
    p1 = head
    seen.add(p1.val)
    p2 = p1.next
    while p2:
        while p2 and p2.val in seen:
            p2 = p2.next
        p1.next = p2
        if p2:
            seen.add(p2.val)
            p1 = p1.next
            p2 = p2.next
    return head

def removeDsorted(head: Node):
    # sorted
    # Time - O(n)
    # Space - O(1)
    if not head:
        return
    p1 = head
    p2 = p1.next
    while p2:
        while p2 and p2.val == p1.val:
            p2 = p2.next
        p1.next = p2
        p1 = p1.next
        if p2:
            p2 = p2.next
    return head

test1 = Node(1)
test1.next = Node(3)
test1.next.next = Node(3)
test1.next.next.next = Node(5)
test1.print()
removeD(test1).print()

test1 = Node(1)
test1.next = Node(3)
test1.next.next = Node(3)
test1.next.next.next = Node(5)
test1.print()
removeDsorted(test1).print()

removeDsorted(Node(5)).print()
removeDsorted(Node(None))