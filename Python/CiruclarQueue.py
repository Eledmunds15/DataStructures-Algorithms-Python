# Circular Queue implementation in Python
# k is the max size of the circular queue

class circularQueue():

    def __init__(self, k):
        self.k = k;
        self.queue = [None] * k;
        self.front = self.rear = -1;

    # Insert an element into the circular queue
    def enqueue(self, element):

        # If the queue is full
        if ((self.rear + 1) % self.k == self.front):
            print("Circular Queue is full\n");
        
        # If the queue was initially empty
        elif (self.front == -1):
            self.front = 0;
            self.rear = 0;
            self.queue[self.rear] = element;

        # If the rear pointer is at the end of the queue, insert the element at the front of the queue
        else:
            self.rear = (self.rear + 1) % self.k;
            self.queue[self.rear] = element;

    # Take out a element
    def dequeue(self):

        # Check if the queue is empty
        if (self.front == -1):
            print("The queue is currently empty\n");

        # If the element only has 1 element in it left;
        elif (self.front == 0) and (self.rear == 0):
            temp = self.queue[self.front];
            self.front = self.rear = -1;
            return temp;
        else:
            temp = self.queue[self.front];
            self.front = (self.front + 1) % self.k;
            return temp;

    def showQueue(self):

        # If the queue is empty
        if (self.front == -1):
            print("The queue is currently empty\n");

        # If the rear pointer is ahead of the front pointer 
        elif (self.rear >= self.front):
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ");
            print("\n");
        
        else:
            for i in range(self.front, self.k):
                print(self.queue[i], end = " ");
            for i in range(0, self.front):
                print(self.queue[i], end = " ");
            print("\n");

circQ = circularQueue(4);
circQ.enqueue(3);
circQ.enqueue(4);
circQ.enqueue(10);
circQ.enqueue(7);
circQ.enqueue(16);

circQ.showQueue();

circQ.dequeue();

circQ.showQueue();



    