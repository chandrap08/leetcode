class Tree(object):
    def __init__(self):
        self.stack = []

    def breadth_first(self,root):
        n = root
        self.stack.append(root.data)
        child_stack =[]
        for c in n.get_children():
            child_stack.append(c)
        while child_stack:
            for c in child_stack:
                self.breadth_first(c)
        return self.stack

    def make_test_tree(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        f = Node("f")
        g = Node("g")
        b.add_child(d,e)
        a.add_child(b,c)
        c.add_child(f,g)
        print a.get_children()
        return a

class Node(object):
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,left,right):
        self.left = left
        self.right =right

    def get_children(self):
        children = [self.left,self.right]
        return children

if __name__ == "__main__":
    t = Tree()
    root = t.make_test_tree()
    s = t.breadth_first(root)
    print s


