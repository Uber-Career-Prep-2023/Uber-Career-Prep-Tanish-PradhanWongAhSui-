# Uses doubly linked list forward-backward two pointer technique
# Time complexity - O(n)
# Space complexity - O(1) - does not use extra space
from DoublyLinkedList import Node

def isPalindrome(head: Node) -> bool:
    if not head:
        return True #should empty doubly linked list return true or false?
    p1, p2 = head, head
    while p2.next:
        p2 = p2.next
    while p1 != p2:
        if p1.val != p2.val:
            return False
        p1 = p1.next
        p2 = p2.prev
    return True

test_node1 = Node(9)
test_node1.insertAtBack(2)
test_node1.insertAtBack(4)
test_node1.insertAtBack(2)
test_node1.insertAtBack(9)
print(isPalindrome(test_node1))

test_node2 = Node(9)
test_node2.insertAtBack(12)
test_node2.insertAtBack(4)
test_node2.insertAtBack(2)
test_node2.insertAtBack(9)
print(isPalindrome(test_node2))

print(isPalindrome(None))

test_node3 = Node(9)
test_node3.insertAtBack(4)
test_node3.insertAtBack(4)
test_node3.insertAtBack(9)
print(isPalindrome(test_node3))

test_node4 = Node(9)
test_node4.insertAtBack(4)
test_node4.insertAtBack(4)
test_node4.insertAtBack(9)
test_node4.insertAtBack(0)
print(isPalindrome(test_node4))
    
test_node5 = Node(9)
test_node5.insertAtBack(4)
test_node5.insertAtBack(3)
test_node5.insertAtBack(9)
print(isPalindrome(test_node5))

test_node6 = Node(10)
print(isPalindrome(test_node6))

test_node7 = Node(10)
test_node7.insertAtBack(10)
print(isPalindrome(test_node7))

test_node8 = Node(10)
test_node8.insertAtBack(9)
print(isPalindrome(test_node8))

# took 16 minutes