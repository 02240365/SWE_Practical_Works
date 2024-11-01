# Singly Linked List Implementation 

This practical contains a simple implementation of a singly linked list in Python. It provides various methods to manipulate and interact with the linked list, including appending nodes, inserting at specific positions, deleting nodes, searching for values, reversing the list, and merging two sorted linked lists.

## Features

- **Node Class**: Represents an individual node in the linked list.

- **LinkedList Class**: Implements the linked list with several methods:

  - `append(data)`: Adds a new node with the specified data to the end of the list.

  - `insert(data, position)`: Inserts a new node at a specified position.

  - `delete(data)`: Removes the first node with the specified data.

  - `search(data)`: Searches for a node containing the specified data and returns its position.

  - `display()`: Displays the contents of the linked list in a user-friendly format.

  - `reverse()`: Reverses the linked list in place.

  - `find_middle()`: Finds and returns the middle element of the linked list.

  - `has_cycle()`: Detects if the linked list contains a cycle.

  - `remove_duplicates()`: Removes duplicate values from the linked list.
  
  - `merge_sorted(other_list)`: Merges two sorted linked lists into one sorted linked list.

## Usage

### Creating a Linked List

```python
# Create a new linked list
ll = LinkedList()

# Append values to the list
ll.append(1)
ll.append(2)
ll.append(3)

# Display the linked list
ll.display()  # Output: 1 -> 2 -> 3
