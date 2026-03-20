class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    
def cicular_linked_list(head):
    slow=head
    fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if fast==slow:
            print("this is circular")
            return True
    print("This is not circular")
    return False

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
# node5.next = node3

cicular_linked_list(node1)

