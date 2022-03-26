# Data Structures And Algorithms

Here are some notes on Data Structures and Algorithms. I've implemented all of them in Python and will attempt to do so in C++ also.

## Types of Data Structures
1. Linear Data Structures
2. Non-Linear Data Structures

## Linear Data Structures
1. Array Data Structure
2. Stack Data Structure
3. Queue Data Structure
4. Linked List Data Structure

## Non-Linear Data Structures
1. Graph Data Structure (Many types)
2. Trees Data Structure (Many types)

## Linear vs Non-Linear Data Structures
Linear Data Structures are arranged in sequential order one after another, in which you can traverse through the array in a single run. The memory utilisation is not as efficient as Non-Linear Data Structures and has a increasing time complexity as the size of the array grows.

Non-Linear Data Structures are not arranged in non-sequential order (hirearchical structure) often containing multiple layers. It might not be possible to traverse through all the elements in the data structure in a single pass, because of the difference between layers. Different data structures utilise memory in different efficient ways (compared to linear data structures) as time complexity is independent of data structure size.

## Asymptotic Notations and Master Theorem

Asymptotic Notations: Mathematical notation used to describe the time complexity (run time) of a particular algorithm. Three main notations: Big-O notation, Omega notation, Theta notation.

Big-O notation: The upper bound of the run-time of an algorithm i.e. Worst Case Scenario.

Omega notation: The lower bound of the run-time of an algorithm i.e. Best Case Scenario.

Theta notation: The upper and lower bound simultaneously i.e. Average Case Scenario.

NOTE: We are almost always only interested in Big-O Notation because we know that all other cases will perform better than this case. I suppose it's probably to do with risk management (If your worse case scenario is good, your average and best case are also probably good, if not better).

Master Theroem: A formula to use when finding the time complexity of recurrence relations (recursive functions).

T(n) = aT(n/b) + f(n);

n = size of input;
a = number of sub-problems needed to solve;
n/b = size of each sub-problem. All sub-problems assumed to have same size.
f(n) = cost of the work done outside of the recursive call, which includes cost of dividing the prolem and merging the solutions together.

## Divide & Conquer
A problem solving strategy that involves breaking a larger problem down into a set of smaller sub-problems. Often times, recursion is used in the divide and conquer strategy.

1: Divide the problem into sub-problems using recursion.
2: Solve the smaller sub-problems recursively. If it's small enough then you can just solve it directly.
3: Combine the solutions of the sub-problems that are part of the recursive process to solve the actual problem.

## Divide & Conquer vs Dynamic Programming
In D&C, by dividing the problem into smaller subproblems and solving them recursively, you don't store the value of each sup-problem, whereas with dynamic programming, you tend to store the value of each sub-problem.

Because of this, if you expect to use the result of a sub-problem in the future, then dynamic programming is probably the best option. However, in the interest of saving storage space, it's best to use the D&C strategy if a sub-problem doesn't have to be solved more than once.

## Advantages of Divide and Conquer Algorithms
- Complexity for multiplication of two matrices (using naive method) is O(n^3). With D&C
- Suitable for multiprocessing systems
- Makes efficient use of memory caches

# Data Structures (I)
## Stack Data Structure

A Stack is a linear data structure the follows LIFO (Last In First Out). It's like having a barrel full of basketballs. In order to get the basketball at the bottom of the barrel, you first have to take out all the basketballs on top of it. 

Basic Operations of Stack:
- Push: Add an element to the top of the Stack.
- Pop: Remove and element from the top of a Stack.
- IsEmpty: Check if the stack is empty.
- IsFull: Check if the stack is full.
- Peek: Get the value of the top element without removing it.

Working of Stack Data Structure:
- A pointer called 'TOP' is used to keep track of the top element in the stack.
- When initializing the stack, we set its value to -1 so that we can check if the stack is empty by comparing 'TOP == -1'.
- On pushing an element, we increase the value of TOP and place the new element in the position pointed to by TOP. Check if the stack is full before pushing an element.
- On popping an element, we decrease the value of TOP and remove the last element. Check if the stack is empty before popping an element.

Applications of Stack Data Structure:
- To reverse a word: Put all the letters in a stack and then pop them out into another list. O(n^2) complexity.
- In web-browsers: Back button pops the last web-url you visited and then visits it. Each time you visit a new page it's added on to the stack.
- When writing a function for a UAV to visit a bunch of destinations and having it go to each location before coming back.

## Queue Data Structure
Similar to the ticket queue outside a cinema hall, where the first person entering the queue is the first person who takes the ticket. Queue follows FIFO (First In First Out) rule, where the item that first goes in is the first time to come out.

Basic Operations of Queue:
- Enqueue: Add an element to the end of the queue.
- Dequeue: Remove an element from the front of the queue.
- IsEmpty: Check if the queue is empty.
- IsFull: Check if the queue is full.
- Peek: Get the value of the front of the queue without removing it.

## Types of Queues
Four different types of queues:
- Simple Queue
- Circular Queue
- Priority Queue
- Double Ended Queue

### Simple Queue
- Insertion takes place at the rear and removal occurs at the front. Follows FIFO (First In First Out)

### Ciruclar Queue
- Last element points to the first element making a circular link.
- Main advantage of a circular queue is better memory utilization. If last position is full and first is empty we can insert the element into the first position.

### Priority Queue
- Each element sassociated with a pariority and is served according to its priority.
- If elements have the same priority then they are served according to that priority.

### Deque (Double Ended Queue)
- Insertion and removal of elements can be performed from either the front or the rear. Thus, it no longer follows FIFO

## Ciruclar Queue
Circular queues are extended versions of regular queues, where the last element is connected to the first element. Solves the problem of having non-usable empty space in the data structure (e.g. after a while the data structure will have empty space is indexes 0, 1, 2 as elements are dequeued).

Circular Queue Operations:
- Two pointers FRONT and REAR
- FRONT tracks the first element of the queue
- REAR tracks the last element of the queue
- Initially, set the value of FRONT and REAR to -1

Enqueue Operation:
- Check if the queue is full
- For the first element, set value of FRONT to 0
- Circularly increase the REAR index to 1 (i.e. if it reaces the end, it would next be at the start of the queue)
- Add the new element in the position pointed to by REAR

Dequeue Operation
- Check if the queue is empty
- Return the value pointed by FRONT
- Circularly increase the FRONT index by 1
- For the last element, reste the values of FRONT and REAR to -1

## Priority Queue
Each element is associated with a priority value and elements are served in queue order on the basis of their priority.

Usually, the value for the element itself is considered for assigning the priority. E.g. highest number is higher priority, or lowest number is highest priority. We can set this priority to be different based on our needs.

Priority Queue Impementation:
- Can be implemented using an array, linked list, heap data structure or binary search tree. Heap data structures is the most efficient out of these.

#NOTE: Since the heap data structure is most efficient, will use this first. Othe data structures used to create queues will be disucssed later.

Priority Queue Operations:
- Insert element from queue
- Deleting an element from queue
- Peeking from the priority queue (Find max/min)
- Extract-max-min from queue

Insert element into queue:
1. Insert the new element a the end of the tree
2. Heapify the tree

Deleteing an element from the queue:
1. Select the element to be deleted
2. Swap it with the last element
3. Remove the last element
4. Heapify the tree

Peeking from priority Queue:
1. Returns the max element from Max Heap or minimum element from Min Heap (basically return rootNode)

Extract-Max/Min from Priority Queue;
1. Return the value of the maxnode/minnode then delete it from the queue.

## Deque Data Structure
Double Endede Queues have insertion and removal of elements at both the front and rear. Does not follow FIFO.

Types of Deque:
- Input Restricted Deque: input is restricted at a single end but allows deletion at both the ends.
- Output Restricted Deque: output is restricted at a single end by allows insertion at both ends.

Opeartions in Deque:
- Insert at the FRONT
- Insert at the REAR
- Delete from the FRONT
- Delete from the REAR

# Data Structures (II)
## Linked List Data Structure
Linear data structure that incldes a series of connected nodes. Each nodes stores data and the address of the next node.

Since the data structure is linear, it has to have a start and an end. The starting node is called HEAD and the final node points to NULL value.

Linked lists can be of multiple types: Singly, Doubly and Circular Linked Lists. 

Operations in Linked Lists:
- Traversal: access each element of a linked list.
- Insertion: adds a new element to the linked list.
- Deletion: removes the existing elements.
- Search: find a node in a linked list.
- Sort: sort the nodes of a linked list.

## Types of Linked Lists
3 main types of Linked Lists
- Singly Linked List: Most common. One node points to another node.
- Doubly Linked List: Now each node points to the previous node and to the next node.
- Circular Linked List: Last element points to the first element.

## Hash Tables





