class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

class Solution(object):

    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        l = LinkedList()
        for k,v in pairs:
            l.push(k)
            l.push(v)

        current = l.head
        nextNode = current
        count = 0

        while nextNode != None:
            current = nextNode
            nextNode = current.next
            if current.data < nextNode.data:
                count += 1
                continue

        return count

if __name__ == "__main__":
    s = Solution()
    l = s.findLongestChain([[1,2], [2,3], [3,4]])
    if l:
        print l
    else:
        print 0
