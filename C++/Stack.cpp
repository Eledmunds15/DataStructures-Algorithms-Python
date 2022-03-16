// Implementing a Stack Data Structure using C++

#include <iostream>

using namespace std;

class Stack
{
  int top;
	public;
	int a[10]; //
	Stack() {
		top = -1;
	}

	void push(int x);
	int pop();
	void isEmpty();
	void isFull();
};

// Function to push data into stack
void Stack::push(int x) {
	if (top >= 10) {
		cout << "Stack Overflow \n"
	}
	else 
	{
		a[++top] = x;
		cout << "Element Inserted \n"
	}
};

void Stack::pop() {
	if (top < 0) {
		cout << "Stack Underflow \n"
			return 0;
	}
	else 
	{
		int d = a[top--];
		return d;
	}
};

void Stack::isEmpty() {
	if (top < 0) 
	{
		cout << "Stack is empty \n";
	}
	else
	{
		cout << "Stack is not empty \n";
	}
}

void Stack::isFull() {
	if (top > 10) {
		cout << "Stack is full \n";
	} 
	else
	{
		cout << "Stack is not full \n"
	}
}

int main() {
	
	Stack S1;
	S1.push(99);
	S1.push(999);
	S1.push(9999);

	S1.push(10000);
	S1.pop();

	S1.isEmpty();
	}
};

