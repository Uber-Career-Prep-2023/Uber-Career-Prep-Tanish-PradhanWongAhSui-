# Uses the linked list fixed-distance two pointer technique
# Time complexity - O(n)
# Space complexity - O(1) 

from SinglyLinkedList import Node

def move_to_front(head: Node, k: int) -> Node:
    # assumes that invalid k will simply return original linked list
    if not head or k < 1:
        return head
    p1 = head
    p2 = head
    for i in range(k):
        p2 = p2.next
        if not p2:
            return head 
    while p2.next:
        p1 = p1.next
        p2 = p2.next
    new_head = p1.next
    p1.next = new_head.next
    new_head.next = head
    return new_head

test_node1 = Node(15)
test_node1.insertAtBack(2)
test_node1.insertAtBack(8)
test_node1.insertAtBack(7)
test_node1.insertAtBack(20)
test_node1.insertAtBack(9)
test_node1.insertAtBack(11)
test_node1.insertAtBack(6)
test_node1.insertAtBack(19)
test_node1.print()
move_to_front(test_node1, 2).print()

test_node2 = Node(15)
test_node2.insertAtBack(2)
test_node2.insertAtBack(8)
test_node2.insertAtBack(7)
test_node2.insertAtBack(20)
test_node2.insertAtBack(9)
test_node2.insertAtBack(11)
test_node2.insertAtBack(6)
test_node2.insertAtBack(19)
move_to_front(test_node2, 7).print()
test_node1.print()

move_to_front(Node(), 3).print()
move_to_front(Node(), 0).print()
move_to_front(Node(), 1).print()
move_to_front(None, 19)

test_node3 = Node(10)
test_node3.insertAtBack(2)
test_node3.insertAtBack(18)
test_node3.insertAtBack(9)
move_to_front(test_node3, 3).print()

test_node3 = Node(10)
test_node3.insertAtBack(2)
test_node3.insertAtBack(18)
test_node3.insertAtBack(9)
move_to_front(test_node3, 4).print()

test_node3 = Node(10)
test_node3.insertAtBack(2)
test_node3.insertAtBack(18)
test_node3.insertAtBack(9)
move_to_front(test_node3, 5).print()

# Test empty linked list
assert move_to_front(None, 1) is None

# Test k is less than 1
test_node2 = Node(1)
test_node2.insertAtBack(2)
test_node2.insertAtBack(3)
test_node2_result = move_to_front(test_node2, 0)
assert test_node2_result == test_node2

# Test k is greater than length of linked list
test_node3 = Node(1)
test_node3.insertAtBack(2)
test_node3.insertAtBack(3)
test_node3_result = move_to_front(test_node3, 4)
assert test_node3_result == test_node3

# Test negative nodes
test_node4 = Node(-1)
test_node4.insertAtBack(-2)
test_node4.insertAtBack(-3)
test_node4.insertAtBack(-4)
test_node4_result = move_to_front(test_node4, 2)
assert test_node4_result.val == -3
assert test_node4_result.next.val == -1
assert test_node4_result.next.next.val == -2
assert test_node4_result.next.next.next.val == -4
assert test_node4_result.next.next.next.next is None

# Test k is 1
test_node5 = Node(1)
test_node5.insertAtBack(2)
test_node5.insertAtBack(3)
test_node5_result = move_to_front(test_node5, 1)
assert test_node5_result.val == 3
assert test_node5_result.next.val == 1
assert test_node5_result.next.next.val == 2
assert test_node5_result.next.next.next is None

# Test k is equal to length of linked list
test_node6 = Node(1)
test_node6.insertAtBack(2)
test_node6.insertAtBack(3)
test_node6_result = move_to_front(test_node6, 3)
assert test_node6_result.val == 1
assert test_node6_result.next.val == 2
assert test_node6_result.next.next.val == 3
assert test_node6_result.next.next.next is None

# Test k is in the middle of linked list
test_node7 = Node(1)
test_node7.insertAtBack(2)
test_node7.insertAtBack(3)
test_node7.insertAtBack(4)
test_node7.insertAtBack(5)
test_node7.insertAtBack(6)
test_node7_result = move_to_front(test_node7, 3)
assert test_node7_result.val == 4
assert test_node7_result.next.val == 1
assert test_node7_result.next.next.val == 2
assert test_node7_result.next.next.next.val == 3
assert test_node7_result.next.next.next.next.val == 5
assert test_node7_result.next.next.next.next.next.val == 6
assert test_node7_result.next.next.next.next.next.next is None

# took 32 minutes
