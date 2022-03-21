# Data Structures And Algorithms

As an Aerospace Engineering student, I'm not taught much about software and how to solve complex problems using software efficiently. Because of this, I thought I'd learn the basics of Data Structures and Algorithms, because I think it'd contribute to my ability to use computer science/software engineering to solve aerospace problems in the future.

I think this is one the first steps in my journey. In the future, I hope to investigate a lot more about software, such as systems design and development, robotics as well as AI.

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
Circular queus are extended versions of regular queues, where the last element is connected to the first element. Solves the problem of having non-usable empty space in the data structure (e.g. after a while the data structure will have empty space is indexes 0, 1, 2 as elements are dequeued).

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





