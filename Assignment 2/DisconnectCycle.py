# Uses the hash linked list nodes technique
# Time complexity - O(n)
# Space complexity - O(n)
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

# Test Case 1
# Empty linked list
test_node1 = None
disconnect_cycle(test_node1)

# Test Case 2
# Linked list with no cycle
test_node2 = Node(1)
test_node2.insertAtBack(2)
test_node2.insertAtBack(3)
test_node2.insertAtBack(4)
test_node2.insertAtBack(5)
disconnect_cycle(test_node2).print()

# Test Case 3
# Linked list with a cycle
test_node3 = Node(1)
test_node3.insertAtBack(2)
test_node3.insertAtBack(3)
test_node3.insertAtBack(4)
test_node3.insertAtBack(5)
test_node3.next.next.next.next.next = test_node3.next.next
disconnect_cycle(test_node3).print()

# Test Case 4
# Linked list with negative node
test_node4 = Node(-1)
test_node4.insertAtBack(-2)
test_node4.insertAtBack(-3)
test_node4.insertAtBack(-4)
test_node4.insertAtBack(-5)
test_node4.next.next.next.next.next = test_node4.next.next
disconnect_cycle(test_node4).print()

# Test Case 5
# Linked list with None node
test_node5 = Node(None)
test_node5.insertAtBack(None)
test_node5.insertAtBack(None)
test_node5.insertAtBack(None)
test_node5.insertAtBack(None)
test_node5.next.next.next.next.next = test_node5.next.next
disconnect_cycle(test_node5).print()

# Took 21 minutes
