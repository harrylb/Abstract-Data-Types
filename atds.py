#!/usr/bin/env python3

class Stack(object):

    def __init__(self):
        self.items = []

    def push(self, item):
         self.items.append(item)

    def pop(self):
         return self.items.pop()

    def peek(self):
         return self.items[len(self.items)-1]

    def size(self):
         return len(self.items)

    def isEmpty(self):
         return self.items == []

class Queue(object):

    def __init__(self):
        self.items = []

    def enqueue(self, item):
         self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def peek(self):
         return self.items[len(self.items)-1]

    def size(self):
         return len(self.items)

    def isEmpty(self):
         return self.items == []

class Deque(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, new_data):
        self.data = new_data

    def setNext(self, new_next):
        self.next = new_next

class UnorderedList(object):
    def __init__(self):
        self.head = None

    def remove(self, item):
        current = self.head
        previous = None
        while current != None:
            if current.getData() == item:
                if previous == None:
                    self.head = current.getNext()
                else:
                    previous.setNext(current.getNext())
                current = current.getNext()
            else:
                previous = current
                current = current.getNext()

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def length(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        while current != None:
            if current.getData() == item:
                found = True
                return True
            else:
                current = current.getNext()
        return False

    def append(self, item):
        current = self.head
        if current:
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(Node(item))
        else:
            self.head = Node(item)

    def index(self, item):
        current = self.head
        counter = 0
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                counter +=1
                current = current.getNext()
        return counter

    def insert(self, pos, item):
        position = 0
        current = self.head
        previous = None
        while position < pos:
            previous = current
            current = current.getNext()
            position +=1
        new_node = Node(item)
        new_node.setNext(current)
        if previous != None:
            previous.setNext(new_node)
        else:
            self.head = new_node

    def pop(self, index=-1):
        if index == -1:
            index = self.length() - 1
        position = 0
        previous = None
        current = self.head
        while position < index:
            previous = current
            current = current.getNext()
            position += 1
        item = current.getData()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        return item

    def __repr__(self):
        """Creates a representation of the list suitable for printing,
        debugging.
        """
        result = "UnorderedList["
        nextNode = self.head
        while nextNode != None:
            result += str(nextNode.getData()) + ","
            nextNode = nextNode.getNext()
        if result[-1] == ",":
            result = result[:-1] # remove trailing comma
        result = result + "]"
        return result


class UnorderedListStack(object):
    def __init__(self):
        self.list = UnorderedList()

    def push(self, data):
        self.list.add(data)

    def pop(self):
        return self.list.pop(0)

    def peek(self):
        last_value = self.list.pop(0)
        self.list.push(last_value)
        return last_value

    def size(self):
        return self.list.length()

    def isEmpty(self):
        return self.list.isEmpty()

    def __repr__(self):
        return self.list.__repr__()

class OrderedList(object):
    def __init__(self):
        self.head = None

    def add(self,item):
        current = self.head
        previous = None
        end = False
        while current != None and not end:
            if current.getData() > item:
                end = True
            else:
                previous = current
                current = current.getNext()
        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def remove(self, item):
        current = self.head
        previous = None
        while current != None:
            if current.getData() == item:
                if previous == None:
                    self.head = current.getNext()
                else:
                    previous.setNext(current.getNext())
                current = current.getNext()
            else:
                previous = current
                current = current.getNext()

    def search(self,item):
        current = self.head
        found = False
        end = False
        while current != None and not found and not end:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    end = True
                else:
                    current = current.getNext()
        return found

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def index(self, item):
        current = self.head
        counter = 0
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                counter +=1
                current = current.getNext()
        return counter

    def pop(self, index=-1):
        if index == -1:
            index = self.length() - 1
        position = 0
        previous = None
        current = self.head
        while position < index:
            previous = current
            current = current.getNext()
            position += 1
        item = current.getData()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        return item
