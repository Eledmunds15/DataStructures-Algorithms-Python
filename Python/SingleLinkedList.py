class Node:
    def __init__(self, data):
        self.data = data;
        self.next = None;

class SinglyLinkedList:
    def __init__(self):
        self.head = None;

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

        print("Successfully added element: " + str(elem) + " to front\n");

    #Insert after a node
    def insertAfter(self, targNode, elem):
        current = self.head;

        while (current.next.data != targNode):
            current = current.next;
        
        newNode = Node(elem);

        current.next

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

        print("Successfully added element: " + str(elem) + " to the end\n");


    #Delete front
    def deleteFront(self):
        temp = self.head;
        self.head = temp.next;

        print("Successfully removed element: " + str(temp.data) + " from the front\n");

    #Delete a node
    def deleteNode(self, targNode):
        current = self.head;
        while (current.next.data != targNode):
            current = current.next;
        
        current.next = current.next.next;

        print("Successfully removed element: " + str(targNode) + " from the linked list\n");

    #Delete last node
    def deleteLast(self):
        last = self.head;

        #Loop to find the second last node in the linked list
        while (last.next.next):
            last = last.next;
        
        temp = last.next;
        last.next = None

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
    def sortDec(self, head):
        return True;

     #Sort the linked list in Ascending order (Merge sort);
    def sortAsc(self):
        return True;

ls = SinglyLinkedList();
ls.insertFront(1);
ls.insertFront(2);
ls.insertFront(3);
ls.insertFront(4);
ls.insertFront(5);
ls.insertFront(6);

ls.search(3)

ls.insertEnd("SebRock");

ls.traverse();

ls.deleteFront();

ls.traverse();

ls.deleteLast();

ls.traverse();

ls.deleteNode(3);

ls.traverse();
