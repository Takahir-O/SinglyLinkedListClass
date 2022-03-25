class Node:
    def __init__(self,data):
        self.data=data
        self.next = None

class SinglyLinkedList:
    def __init__(self,node):
        self.head = node

node1=Node(7)
node2=Node(99)
node3=Node(45)

numList = SinglyLinkedList(node1)

numList.head.next = node2
numList.head.next.next=node3

currentNode= numList.head
while currentNode is not None:
    print(currentNode.data)
    currentNode=currentNode.next