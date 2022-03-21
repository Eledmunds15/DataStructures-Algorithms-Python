# Priority Queue implmentation with Python

#Function to heapify the tree
def heapify(arr, n, i):
    # Find the largest among root, left child and right child
    largest = i;
    left = 2 * i + 1;
    right = 2 * i - 1;

    if left < n and arr[i] < arr[left]:
        largest = left;

    if right < n and arr[largest] < arr[right]:
        largest = right;

    # Sweap and continue heapifying if root is not the largest
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i];
        heapify(arr, n, largest);

# Function to insert and element into tree
def insertElem(arr, item):
    size = len(arr);
    if size == 0:
        arr.append(item);
    else:
        arr.append(item)
        for i in range((size//2) - 1, -1, -1):
            heapify(arr, size, i);

# Function to delete an element in the tree
def deleteElem(arr, item):
    size = len(arr);
    i = 0;
    for i in range(0, size):
        if item == arr[i]:
            break;
    
    arr[i], arr[size-1] = arr[size-1], arr[i];

    #print(size-1)
    #print(len(arr)-1)
    arr.remove(arr[size-1]);

    for i in range((len(arr) // 2) - 1, -1, -1):
        heapify(arr, len(arr), i);

#Function to remove the first element in the queue
def dequeue(arr):
    item = arr[0];
    deleteElem(arr, item);


e = [];
insertElem(e, 3);
insertElem(e, 18);
insertElem(e, -3);
insertElem(e, 5);
insertElem(e, 8);
insertElem(e, 189);
insertElem(e, -33);
insertElem(e, 52);

print("Max-Heap array: " + str(e) + "\n");

deleteElem(e, 5)

print("Max-Heap array after delete '52': " + str(e) + "\n");

dequeue(e)

print("Max-Heap array after dequeue: " + str(e) + "\n");



