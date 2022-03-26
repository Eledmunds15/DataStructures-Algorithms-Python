from xml.etree.ElementTree import TreeBuilder


class Node:
    def __init__(self, data):
        self.data = data;
        self.next = None;
        self.prev = None;

class DoublyLinkedList:
    def __init__(self):
        self.head = None;

    #Insert at the front
    def insertFront(self, elem):
        #Create new node using elem
        newNode = Node(elem); 

        #Set next pointer of new node to self.head
        newNode.next = self.head

        #Move the self.head pointer back
        if self.head != None:
            self.head.prev = self.head;
        

        self.head = newNode;

        print("Successfully added element: " + str(elem) + " to front\n");
    
    #Insert at the rear
    def insertRear(self, elem):
        #Create new node using elem
        newNode = Node(elem);

        #If list is empty
        if self.head == None:
            self.head = newNode;

        #Iterate to the last node;
        current = self.head;
        while (current.next):
            current = current.next;
        
        #Set the next pointer to 
        current.next = newNode;
        newNode.prev = current;

        print("Successfully added element: " + str(elem) + " to end\n");

    
    #Insert after a node
    def insertAfter(self, targNode, elem):

        if not self.search(targNode):
            print("Target Node needs to be in Linked List...\n");
            return;
        
        current = self.head;
        newNode = Node(elem);

        while (current.data != targNode):
            current = current.next;
        
        temp = current.next.next;

        current.next = newNode;
        newNode.prev = current;
        newNode.next = temp;
        temp.prev = newNode;

        print("Successfully added element: " + str(elem) + " after " + str(targNode) + "\n");
    
    #Remove at the front
    def removeFront(self):
        if self.head == None:
            print("List already currently empty...\n")

        temp = self.head;
        self.head = temp.next;
        self.head.prev = None;

        print("Successfully removed element: " + str(temp.data) + "from start of the list\n");
        
    #Remove at the rear
    def removeRear(self):
        if self.head == None:
            print("List already currently empty...\n")

        last = self.head;

        while (last.next.next):
            last = last.next;

        temp = last.next;
        last.next = None;
        
        print("Successfully removed element: " + str(temp.data) + " from the end\n");

    #Remove after
    def removeAfter(self):
        return True;

    #Search
    def search(self, target):
        current = self.head;
        while(current.next):
            if (current.data == target):
                print(str(target) + "is in the list...\n")
                return True;
            current = current.next;
        print(str(target) + " was not in the list...\n")
        return False;

    def show(self):
        current = self.head;
        while (current):
            print(current.data, end=" ");
            current = current.next;
        print("\n");

    #return ascending order linked list
    def sortAsc(self):
        return True;
    
    #return descending order linked list
    def sortDec(self):
        return True;

ls = DoublyLinkedList();
ls.insertFront(4);
ls.insertFront(4);
ls.insertFront(5);
ls.insertFront(4);
ls.insertFront(4);

ls.insertAfter(5, 6);

ls.insertRear("FinHarps")

ls.removeFront();

ls.removeRear();

ls.show();

ls.search("Shaky")