# Uses linked list reset/catch-up two pointer technique
# Time complexity - O(n)
# Space complexity - O(1)

from SinglyLinkedList import Node

def dedupSort(head: Node):
    if not head:
        return None
    p1 = head
    p2 = head.next
    while p2:
        if p2.val != p1.val:
            p1.next = p2
            p1 = p2
        p2 = p2.next
    p1.next = None
    return head

test_node10 = Node(None)
test_node10.print()
print(dedupSort(test_node10))

print(dedupSort(None))


test_node1 = Node(1)
test_node1.insertAtBack(2)
test_node1.insertAtBack(2)
test_node1.insertAtBack(4)
test_node1.insertAtBack(5)
test_node1.insertAtBack(5)
test_node1.insertAtBack(5)
test_node1.insertAtBack(10)
test_node1.insertAtBack(10)

test_node1.print()
dedupSort(test_node1).print()

test_node2 = Node(8)
test_node2.insertAtBack(8)
test_node2.insertAtBack(8)
test_node2.insertAtBack(8)

test_node2.print()
dedupSort(test_node2).print()

print(dedupSort(None))

test_node3 = Node(-10000)
test_node3.next = Node(-999)
test_node3.next.next = Node(-999)
test_node3.next.next.next = Node(123123)
test_node3.print()
dedupSort(test_node3).print()

# Test case 1
# Expected output: 1->2->3->4->5->None
test_node4 = Node(1)
test_node4.next = Node(1)
test_node4.next.next = Node(2)
test_node4.next.next.next = Node(3)
test_node4.next.next.next.next = Node(3)
test_node4.next.next.next.next.next = Node(4)
test_node4.next.next.next.next.next.next = Node(5)
result1 = dedupSort(test_node4)
while result1:
    print(result1.val, end="->")
    result1 = result1.next
print("None")

# Test case 2
# Expected output: 1->None
test_node5 = Node(1)
test_node5.next = Node(1)
result2 = dedupSort(test_node5)
while result2:
    print(result2.val, end="->")
    result2 = result2.next
print("None")

# Test case 3
# Expected output: 1->2->3->None
test_node6 = Node(1)
test_node6.next = Node(2)
test_node6.next.next = Node(3)
result3 = dedupSort(test_node6)
while result3:
    print(result3.val, end="->")
    result3 = result3.next
print("None")

# Took 25 minutes