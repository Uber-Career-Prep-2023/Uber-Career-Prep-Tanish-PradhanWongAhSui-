# Uses doubly linked list forward-backward two pointer technique
# Time complexity - O(n)
# Space complexity - O(1) - does not use extra space
from DoublyLinkedList import Node

# def isPalindrome(head: Node) -> bool:
#     if not head:
#         return True #should empty doubly linked list return true or false?
#     p1, p2 = head, head
#     while p2.next:
#         p2 = p2.next
#     while p1 != p2:
#         if p1.val != p2.val:
#             return False
#         p1 = p1.next
#         p2 = p2.prev
#     return True

def isPalindrome(head: Node) -> bool:
    if not head:
        return True
    p1, p2 = head, head
    while p2 and p2.next:
        p1 = p1.next
        p2 = p2.next.next
    prev = None
    while p1:
        temp = p1.next
        p1.next = prev
        prev = p1
        p1 = temp
    while prev:
        if prev.val != head.val:
            return False
        prev = prev.next
        head = head.next
    return True

        # 9 - 2 - 4 - 4 - 2 - 9 

test_node1 = Node(9)
test_node1.insertAtBack(2)
test_node1.insertAtBack(4)
test_node1.insertAtBack(2)
test_node1.insertAtBack(9)
assert isPalindrome(test_node1) == True

test_node1 = Node(9)
test_node1.insertAtBack(2)
test_node1.insertAtBack(4)
test_node1.insertAtBack(4)
test_node1.insertAtBack(2)
test_node1.insertAtBack(9)
assert isPalindrome(test_node1) == True

assert isPalindrome(Node(None)) == True

test_node_neg1 = Node(-5)
assert isPalindrome(test_node_neg1) == True

test_node_neg2 = Node(-12)
test_node_neg2.insertAtBack(0)
test_node_neg2.insertAtBack(-12)
assert isPalindrome(test_node_neg2) == True

test_node_neg2 = Node(-12)
test_node_neg2.insertAtBack(0)
test_node_neg2.insertAtBack(-12)
test_node_neg2.insertAtBack(-12)
assert isPalindrome(test_node_neg2) == False


test_node2 = Node(9)
test_node2.insertAtBack(12)
test_node2.insertAtBack(4)
test_node2.insertAtBack(2)
test_node2.insertAtBack(9)
assert isPalindrome(test_node2) == False

assert (isPalindrome(None)) == True

test_node3 = Node(9)
test_node3.insertAtBack(4)
test_node3.insertAtBack(4)
test_node3.insertAtBack(9)
assert (isPalindrome(test_node3)) == True

test_node4 = Node(9)
test_node4.insertAtBack(4)
test_node4.insertAtBack(4)
test_node4.insertAtBack(9)
test_node4.insertAtBack(0)
assert (isPalindrome(test_node4)) == False
    
test_node5 = Node(9)
test_node5.insertAtBack(4)
test_node5.insertAtBack(3)
test_node5.insertAtBack(9)
assert (isPalindrome(test_node5)) == False

test_node6 = Node(10)
assert (isPalindrome(test_node6)) == True

test_node7 = Node(10)
test_node7.insertAtBack(10)
assert (isPalindrome(test_node7)) == True

test_node8 = Node(10)
test_node8.insertAtBack(9)
assert (isPalindrome(test_node8)) == False

# took 25 minutes