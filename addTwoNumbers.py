class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        return

class LinkedList:
    def __init__(self):
        self.head = None

    def addNode(self,data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def printList(self):
         node = self.head
         while node != None:
             print node.data
             node = node.next

    def search(self,k):
        node = self.head
        if node != None:
            while node.next != None:
                if node.data == k:
                    return node
                node = node.next
            if node.data == k:
                return node.data
        return None

if __name__ == "__main__":
    l = LinkedList()
    l.addNode(2)
    l.addNode(3)
    l.addNode(5)
    l.addNode(6)
    print l.printList()
    if(l.search(4)):
        print "found"
    else:
        print "not found"
