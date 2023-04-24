# Uses the hash linked list nodes technique
# Time complexity - O(n)
# Space complexity - O(1)
from SinglyLinkedList import Node

def disconnect_cycle(head: Node) -> Node:
    if not head:
        return None
    map = {head:0}
    curr = head
    while curr.next:
        if curr.next in map:
            curr.next = None
            return head
        map[curr.next] = 0
        curr = curr.next
    return head

test_node1 = Node(10)
test_node1.insertAtBack(18)
cycle_node1 = Node(12)
cycle_node1.next = Node(9)
cycle_node1.next.next = Node(11)
cycle_node1.next.next.next = Node(4)
cycle_node1.next.next.next.next = cycle_node1
test_node1.next.next = cycle_node1
# test_node1.print() 

disconnect_cycle(test_node1).print()

test_node2 = Node(10)
test_node2.insertAtBack(18)
test_node2.insertAtBack(12)
test_node2.insertAtBack(9)
test_node2.insertAtBack(11)
cycle_node2 = Node(4)
cycle_node2.next = cycle_node2
test_node2.next.next.next.next.next = cycle_node2
# test_node2.print() 
disconnect_cycle(test_node2).print()

print(disconnect_cycle(None))

cycle_node3 = Node(8)
cycle_node3.next = cycle_node3
# cycle_node3.print()
disconnect_cycle(cycle_node3).print()

cycle_node4 = Node(12)
cycle_node4.next = Node(9)
cycle_node4.next.next = Node(11)
cycle_node4.next.next.next = Node(4)
cycle_node4.next.next.next.next = cycle_node4
# cycle_node4.print()
disconnect_cycle(cycle_node4).print()

# Took 21 minutes
