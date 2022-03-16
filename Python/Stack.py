from inspect import stack

# Create a stack
def create_stack():
    stack = [];
    return stack;

# State whether stack is empty or not;
def stack_empty(stack):
    return len(stack) == 0;

# Push an item into the stack
def push(stack, item):
    stack.append(item);
    print("Pushed item: " + item + " to stack");

# Pop an element from the stack
def pop(stack):
    item = stack[len(stack)-1];
    stack.pop();
    print("Popped item: " + item + " from stack");

# Show the stack in terminal
def show_stack(stack):
    print(stack);

def peek_stack(stack):
    print(stack[len(stack)-1]);

stack = create_stack();
push(stack, str(1));
push(stack, str(2));
push(stack, str(3));
push(stack, str(4));

peek_stack(stack);
show_stack(stack);
    
    
