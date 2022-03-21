# Implementation of a simple queue in Python

class Queue:

    def __init__(self):
        self.queue = [];

    # Add an element to the queue
    def enqueue(self, element):
        self.queue.append(element);

    # Remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            return None;
        return self.queue.pop(0);
    
    # Display queue
    def displayQueue(self):
        print(self.queue);

    def size(self):
        print(len(self.queue));

ethanQueue = Queue();
ethanQueue.enqueue(1);
ethanQueue.enqueue(2);
ethanQueue.dequeue();
ethanQueue.enqueue(3);

ethanQueue.displayQueue();
ethanQueue.size();