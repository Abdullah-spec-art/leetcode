class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def middlelinkedlist(head):
    slow=head
    fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    if fast:
        slow=slow.next
    return slow

def reverselinkedlist(middle):
    prev=None
    curr=middle
    next=None
    while curr!=None:
        next=curr.next
        curr.next=prev
        prev=curr
        curr=next
    return prev

def ispalindrome(head,reverse):
    half_1st=head
    half_2nd=reverse
    while half_2nd:
        if half_1st.data!=half_2nd.data:
            return "not a palindrome"
        half_1st=half_1st.next
        half_2nd=half_2nd.next
    return "palindrome"
    
        
def traverse(head):
    curr=head
    while curr!=None:
        print(curr.data," -> ",end="")
        curr=curr.next
    



node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(11)
node5 = Node(7)
node6 = Node(7)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6


middle=middlelinkedlist(node1)

reverse=reverselinkedlist(middle)
print("Middle: ")
traverse(head=node1)
print("\nreverse: ")
traverse(reverse)

print(ispalindrome(node1,reverse))
