# Deque implementation in Python

class Deque():

    def __init__(self):
        self.items = [];
    
    def isEmpty(self):
        return self.items == [];

    def addRear(self, item):
        self.items.append(item);

    def addFront(self,item):
        self.items.insert(0,item);

    def removeFront(self):
        self.items.pop(0);

    def removeRear(self):
        self.iterms.pop();

    def show(self):
        print(self.items);
    
    def size(self):
        return len(self.items)

d = Deque();

print(d.isEmpty())

d.addFront(9856);
d.addFront(3123);
d.addRear(6573);

d.show();

d.removeFront();

d.show();