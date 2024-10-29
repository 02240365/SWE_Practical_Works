# Data Structures in Python: Stacks and Queues

This practical provides implementations of basic data structures (Stack and Queue) and demonstrates their applications in solving common problems. This includes algorithms for reversing strings, checking balanced parentheses, simulating the "Hot Potato" game, and evaluating postfix expressions, among other tasks. It includes exercises that further enhance understanding by implementing a task scheduler and a queue using two stacks.

## Features

### Part 1: Stack Implementation
The stack follows a Last-In-First-Out (LIFO) model and includes:

- `is_empty()`: Check if the stack is empty.

- `push(item)`: Add an item to the stack.

- `pop()`: Remove and return the last item from the stack.

- `peek()`: View the top item of the stack without removing it.

- `size()`: Get the number of items in the stack.

#### Example Usage:
```python
stack = Stack()
stack.push(1)
stack.push(2)
print(stack.pop())  # Output: 2
print(stack.peek())  # Output: 1
print(stack.size())  # Output: 1
