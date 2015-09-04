import Queue


class SafeQueue(object):
    safe = Queue.Queue()

    def safe_put(self, data):                    # simple overlay function that prevents non-integer storage
        if type(data) is int:
            self.safe.put(data)
            print "Integer stored!"
        else:
            print "This is not an integer."

    def safe_get(self):
        return self.safe.get()

    def qsize(self):
        return self.safe.qsize()

    def empty(self):
        return self.safe.empty()


class Stack(object):
    stack = []
    count = 0

    def push(self, data):
        if type(data) is int:
            self.stack = self.stack + [data]
            self.count += 1
            print "Integer stored!"
        else:
            print "This is not an integer."

    def pop(self):
        if self.count > 0:
            ret = self.stack[(self.count - 1)]
            del self.stack[(self.count - 1)]
            self.count -= 1
            print "Stack top popped!"
            return ret
        else:
            print "Stack is empty, cannot pop."

    def check_size(self):
        return self.count


class BinaryNode(object):
    key = None
    left = None
    right = None
    parent = None

    def __init__(self, value, parent):
        self.key = value
        self.parent = parent

    def search(self, parentValue):                # self-searching nodes are convenient; search invoked via the tree
        print "%r %r" % (self.key, parentValue)
        if self.key == parentValue:
            return self
        elif (self.key != parentValue) and (self.left is not None):
            return self.left.search(parentValue)
        elif (self.key != parentValue) and (self.right is not None):
            return self.right.search(parentValue)
        else:
            print "None"
            return None

    def cull(self, value):                  # self-deleting nodes are also convenient; delete invoked via the tree
        if self.left is not None:
            if self.left.key == value:
                self.left = None
            else:
                self.left.cull(value)
        if self.right is not None:
            if self.right.key == value:
                self.right = None
            else:
                self.right.cull(value)


class BinaryTree(object):                   # tree starts empty, root node added "manually" post-instancing
    root = None

    def add(self, value, parentValue):
        if (self.root is None) and (parentValue is None):
            self.root = BinaryNode(value, None)
            return True
        else:
            solution = self.root.search(parentValue)
            if solution is not None:
                if solution.left is None:
                    solution.left = BinaryNode(value, parentValue)
                    return True
                elif solution.right is None:
                    solution.right = BinaryNode(value, parentValue)
                    return True
                else:
                    print "Parent has two children, node not added."
                    return False
            else:
                print "Parent not found."
                return False

    def delete(self, value):                # invokes self-deleting process, after ensuring there is a node to delete
        if self.root is None:
            print "Binary Tree is empty, cannot delete further."

        solution = self.root.search(value)
        if solution is None:
            print "Node not found."
        elif (solution.left is not None) or (solution.right is not None):
            print "Node not deleted, has children."
        else:
            self.root.cull(value)

    def print_tree(self):                   # nominal print function that invokes helper via tree root node
        if self.root is None:
            print "Binary Tree is empty."
        self.print_root(self.root)

    def print_root(self, node):             # helper print function that does all the work
        if (node.left is None) and (node.right is None):
            print node.key
        elif (node.left is not None) and (node.right is not None):
            self.print_root(node.left)
            self.print_root(node.right)
        elif node.left is not None:
            self.print_root(node.left)


class Graph(object):
    graph = {}
    verts = 0

    def add_vertex(self, value):
        if self.graph.keys().count(value) == 0:
            self.graph[value] = []
        else:
            print "Vertex already exists."

    def add_edge(self, value1, value2):
        if (value1 is not None) and (value2 is not None):
            self.graph[value1] += [value2]
            self.graph[value2] += [value1]
        elif (value1 is None) or (value2 is None):
            print "One or more vertices not found."
        elif value1 == value2:
            print "Nice try Loopy McLooperson."
        else:
            print "ERROR: Something enigmatic happened."

    def find_vertex(self, value):
        for x in self.graph.keys():
            if x == value:
                print self.graph[value]



# tests exist below this line

# Queue Tests
print "! ! Beginning Queue Tests ! !"
TestQueue = SafeQueue()
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]:  # ints to queue
    TestQueue.safe_put(x)                        # Adding ints to queue
    print "Added %d. " % x
print "Size of queue is now %d. " % TestQueue.qsize()
while TestQueue.empty() is not True:        # Removing queued ints
    z = TestQueue.safe_get()
    print "Removed %d." % z
if TestQueue.empty():
    print "Queue is now empty."             # Double-check of queue emptiness
else:
    print "Queue remains un-empty."
print "! ! Ending Queue Tests ! !"


# Stack Tests
print "! ! Beginning Stack Tests ! !"
TestStack = Stack()
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]:  # ints to stack
    TestStack.push(x)                       # Adding ints to stack
    print "Added %d. " % x
print "Size of stack is now %d. " % TestStack.check_size()
while TestStack.check_size() > 0:           # Removing stacked ints
    y = TestStack.pop()
    print "Popped %d." % y
if TestStack.check_size() == 0:
    print "Stack is now empty."             # Double-check of stack emptiness
else:
    print "Stack remains un-empty."
print "! ! Ending Stack Tests ! !"


# Tree Tests
print "! ! Beginning Tree Tests ! !"
TestTree = BinaryTree()
parentList = {1:None, 2:1, 3:1, 4:2, 5:2, 6:3, 7:3, 8:4, 9:4, 10:5}      # parents to store values under
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:     # values to be stored
    c = TestTree.add(x, parentList[x])    # adding nodes to the tree
    if c:
        print "Added %d to %r." % (x, parentList[x])
    else:
        print "Failed to add %d to %r." % (x, parentList[x])
print "Now printing Binary Tree below:"
TestTree.print_tree()
print "! ! Ending Tree Tests ! !"


# Graph Tests
print "! ! Beginning Graph Tests ! !"
print "! ! Ending Graph Tests ! !"

