class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode


    def search(self,data):
        current = self.head
        while current != None:
            if current.data == data:
                return True
            else:
                current = current.next
        return False

if __name__ == "__main__":
    l = LinkedList()
    #2->3->5->7->9
    l.push(2)
    l.push(3)
    l.push(5)
    l.push(7)
    l.push(9)
    print(l.search(64))
