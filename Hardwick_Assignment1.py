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

    def search(self, value):
        if self.key == value:
            return self
        elif (self.key != value) and (self.left is not None):
            self.search(self.left, value)
        elif (self.key != value) and (self.right is not None):
            self.search(self.right, value)
        return None


class BinaryTree(object):

    def __init__(self):
        self.root = None

    def add(self, value, parentValue):
        if self.root is None and parentValue is None:
            self.root = BinaryNode(value, parentValue)
        else:
            if self.root.search(value) is not None:
                






