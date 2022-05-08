# Implementation of a SinglyLinkedList with Python.

"""
Note: I've included functions to do both mergeSort and bubbleSort.
Merge sort includes functions: sortedMerge, mergeSort and getMiddle.
"""

class Node:
    def __init__(self, data):
        self.data = data;
        self.next = None;

class SinglyLinkedList:
    def __init__(self):
        self.head = None;
        self.length = 0;

    #Traverse the linked list
    def traverse(self):
        current = self.head;

        while current:
            print(current.data, end=" ");
            current = current.next;
        
        print("\n");

    #Insert at the front
    def insertFront(self, elem):
        newNode = Node(elem);

        newNode.next = self.head;
        self.head = newNode;
        self.length += 1;

        print("Successfully added element: " + str(elem) + " to front\n");

    #Insert after a node
    def insertAfter(self, targNode, elem):
        current = self.head;

        while (current.data != targNode):
            current = current.next;
        
        newNode = Node(elem);
        temp = current.next;
        current.next = newNode;
        newNode.next = temp;

        self.length += 1;

        print("Successfully added element: " + str(elem) + " after " + str(temp.data) + "\n");

    #Insert at the end
    def insertEnd(self, elem):
        newNode = Node(elem);

        #Check if linked list is empty
        if self.head == None:
            self.head = newNode;
            return;
        
        #Go to last elem and make its next node element
        last = self.head;
        while (last.next):
            last = last.next;
        last.next = newNode;
        self.length += 1;

        print("Successfully added element: " + str(elem) + " to the end\n");


    #Delete front
    def deleteFront(self):
        temp = self.head;
        self.head = temp.next;
        self.length -= 1;

        print("Successfully removed element: " + str(temp.data) + " from the front\n");

    #Delete a node
    def deleteNode(self, targNode):
        current = self.head;
        while (current.next.data != targNode):
            current = current.next;
        
        current.next = current.next.next;
        self.length -= 1;

        print("Successfully removed element: " + str(targNode) + " from the linked list\n");

    #Delete last node
    def deleteLast(self):
        last = self.head;

        #Loop to find the second last node in the linked list
        while (last.next.next):
            last = last.next;
        
        temp = last.next;
        last.next = None
        self.length -= 1;

        print("Successfully removed element: " + str(temp.data) + " from the end\n");

    #Search for a node (returns whether it is or isnt in the list)
    def search(self, elem):
        current = self.head;

        while current:
            if current.data == elem:
                print(str(elem) + " present\n")
                return True;
            
            current = current.next
        
        print(str(elem) + " not present\n");
        return False;

    #Sort the linked list in Descending order
    def sortedMerge(self, a, b):
        result = None;

        #Base cases
        if a == None:
            return b;
        if b == None:
            return a;

        # pick either a or b and recur
        if (a.data <= b.data):
            result = a;
            result.next = self.sortedMerge(a.next, b);
        else:
            result = b;
            result.next = self.sortedMerge(a, b.next);

        return result;

    def mergeSort(self, h):
        if h == None or h.next == None:
            return h;
        
        middle = self.getMiddle(h);
        nexttomiddle = middle.next;

        middle.next = None;

        #Appyl mergeSort to right and left of the lists
        left = self.mergeSort(h);
        right = self.mergeSort(nexttomiddle);

        #Merge the left and right lists
        sortedList = self.sortedMerge(left, right);

        return sortedList;
    
    # Function to find the middle of the linked list
    def getMiddle(self, head):
        if (head == None):
            return head;

        slow = head;
        fast = head;

        # For every time the slow pointer moves forward, the fast pointer moves forward by two spaces. When the forward pointer reaches the end, the slow pointer will be in the middle.
        while(fast.next != None and fast.next.next != None):
            slow = slow.next;
            fast = fast.next.next;
        
        return slow;


ls = SinglyLinkedList();
ls.insertFront(6);
ls.insertFront(5);
ls.insertFront(4);
ls.insertFront(3);
ls.insertFront(2);
ls.insertFront(1);

ls.insertAfter(2, 7);

ls.traverse();

ls.head = ls.mergeSort(ls.head);

ls.traverse();