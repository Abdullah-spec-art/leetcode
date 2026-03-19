class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    
def reverseList(head):
        prev=None
        curr=head
        next=None
        while curr!=None:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        return prev

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5



def printlist(head):
    curr=head
    while curr:
            print(curr.data,"-> " ,end="")
            curr=curr.next
    print("None")


print("Original list: ")
printlist(node1)
#reverse list
new_head = reverseList(node1)
print("Reverse list: ")
printlist(new_head)