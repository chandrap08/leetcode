class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.stack = {}
        self.accessed = []

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.accessed:
            i = self.accessed.index(key)
            self.accessed = self.accessed[:i] + self.accessed[i + 1:]
        self.accessed.append(key)
        if len(self.accessed) > self.capacity:
            del self.accessed[0]

        if key in self.stack.keys():
            return self.stack[key]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        # print(self.stack)
        if key in self.accessed:
            i = self.accessed.index(key)
            if i < len(self.accessed) -1:
                self.accessed = self.accessed[:i] + self.accessed[i + 1:]
            return self.stack[key]
        self.accessed.append(key)
        if len(self.accessed) > self.capacity:
            del self.stack[self.accessed[0]]
            self.accessed = self.accessed[1:]
        self.stack[key] = value


if __name__ == "__main__":

#[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
        capacity = 2
        obj = LRUCache(capacity)
        obj.put(2, 6)
        obj.get(1)
        obj.put(1, 5)
        obj.get(1)
        obj.put(3, 3)

        obj.get(2)
        obj.put(4, 4)

        obj.get(1)
        obj.get(3)
        obj.get(4)


