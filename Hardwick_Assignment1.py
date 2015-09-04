import Queue


class Queue(object):
    def add(self, data):
        if data.type() is int:
            self.put(data)
            print "Integer stored!"
        else:
            print "This is not an integer."


class Stack(object):
    stack = []
    count = 0

    def push(self, data):
        if data.type() is int:
            self.stack + [data]
            self.count += 1
            print "Integer stored!"
        else:
            print "This is not an integer."

    def pop(self):
        if self.count > 0:
            del self.list[self.count - 1]
            self.count -= 1
            print "Stack top popped!"
        else:
            print "Stack is empty, cannot pop."

    def checkSize(self):
        return self.count


class BinaryNode(object):

    def __init__(self, key, parent):
        self.key = key
        self.left = None
        self.right = None
        self.parent = parent

    def search(self, value):                # self-searching nodes are convenient; search invoked via the tree
        if self.key == value:
            return self
        elif (self.key != value) and (self.left is not None):
            self.search(self.left, value)
        elif (self.key != value) and (self.right is not None):
            self.search(self.right, value)
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

    def __init__(self):
        self.root = None

    def add(self, value, parentValue):
        if self.root is None and parentValue is None:
            self.root = BinaryNode(value, None)
        else:
            solution = self.root.search(value)
            if solution is not None:
                if solution.left is None:
                    solution.left = BinaryNode(value, solution.left)
                elif solution.right is None:
                    solution.right = BinaryNode(value, solution.right)
                else:
                    print "Parent has two children, node not added."
            else:
                print "Parent not found."

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
