class circDeque():

    def __init__(self,size):
        self.size = size;
        self.queue = [None] * size;
        self.front = self.rear = -1;

    # Insert element at front pointer
    def fInsert(self, elem):
        # Check if the queue is full
        if ((self.rear + 1) % self.size == self.front):
            print("Error: Queue is full\n");
        # Check if the queue is empty
        elif (self.front < 1):
            self.front = self.size - 1;
            self.queue[self.front] = elem;
            print(str(elem) + " successfully added\n");
        else:
            self.front -= 1;
            self.queue[self.front] = elem;
            print(str(elem) + " successfully added\n");

    # Insert element at rear pointer
    def rInsert(self, elem):
        # Check if the queue is full
        if ((self.rear + 1) % self.size) == self.front:
            print("Error: Queue is full\n");
        elif (self.front == -1):
            self.front = self.rear = 0;
            self.queue[self.rear] = elem;
            print(str(elem) + " successfully added\n");
        # Check if the rear pointer is at the end of the queue
        elif (self.rear - 1 == self.size):
            self.tail = 0;
            self.queue[self.rear] = elem;
            print(str(elem) + " successfully added\n");
        else:
            self.rear += 1;
            self.queue[self.rear] = elem;
            print(str(elem) + " successfully added\n");

    # Delete element at front pointer
    def fDelete(self):
        # Check if the front is empty
        if (self.front == -1):
            print("Error: Queue is empty\n");
        # Check if its the last element
        elif (self.front == self.rear):
            temp = self.queue[self.front];
            self.front = self.rear = -1;
            print(temp + " successfully removed\n");
        elif (self.front - 1) == self.size:
            temp = self.queue[self.front];
            self.front = 0;
            print(temp + " successfully removed\n");
        else:
            temp = self.queue[self.front];
            self.front = (self.front + 1) % self.size;
            print(temp + " successfully removed\n");

    # Delete element at rear pointer
    def rDelete(self):
        # Check if the front is empty
        if (self.front == -1):
            print("Error: Queue is empty\n");
        # Check if its the last element
        elif (self.front == self.rear == 0):
            temp = self.queue[self.rear];
            self.front = -1;
            print(temp + " successfully removed\n");
        else:
            temp = self.queue[self.front];
            self.rear = (self.rear - 1) % self.size;
            print(temp + " successfully removed\n");

    # Show the array
    def show(self):
        # If the queue is empty
        if (self.front == -1):
            print("The queue is currently empty\n");

        # If the rear pointr is ahead of the front pointer
        elif (self.rear >= self.front):
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ");
            print("\n");
        
        else:
            for i in range(self.front, self.size):
                print(self.queue[i], end=" ");
            for i in range(0, self.front):
                print(self.queue[i], end=" ");
            print("\n");

CDQ = circDeque(4);

CDQ.rInsert("Shaky")
CDQ.rInsert("Arthit")

CDQ.show();

CDQ.fDelete();
CDQ.fInsert("Bolun");
CDQ.fInsert("Fin");
CDQ.fInsert("Shaky")

CDQ.show();