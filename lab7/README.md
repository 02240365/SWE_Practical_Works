# Binary Search Tree (BST) Implementation in Python

This practical provides a Python implementation of a Binary Search Tree (BST) with various essential operations. The BST is implemented using two classes:

1. `Node` - Represents a single node in the BST.

2. `BinarySearchTree` - Implements the BST structure with methods for inserting, deleting, and traversing nodes, among other features.

## Features

This implementation includes the following features:

### 1. **Insertion**
   - Insert a new value into the BST, maintaining the binary search property.

### 2. **Search**
   - Search for a specific value in the BST. Returns `True` if found, otherwise `False`.

### 3. **Deletion**
   - Remove a specified node from the BST, adjusting the tree to maintain its structure.

### 4. **Traversals**
   - **In-order Traversal**: Visit nodes in ascending order.
   - **Pre-order Traversal**: Visit nodes in root-left-right order.
   - **Post-order Traversal**: Visit nodes in left-right-root order.
   - **Level-order Traversal**: Visit nodes level by level (breadth-first search).

### 5. **Maximum Value**
   - Find the maximum value present in the BST.

### 6. **Node Count**
   - Count the total number of nodes in the BST.

### 7. **Height of the BST**
   - Calculate the height (or depth) of the BST, defined as the longest path from the root to a leaf.

### 8. **Validity Check**
   - Check if the BST satisfies the binary search tree property.

## Usage Example

Below is an example of how to use the `BinarySearchTree` class with common operations:

```python
if __name__ == "__main__":
    bst = BinarySearchTree()
    
    # Insert values
    for value in [5, 3, 7, 2, 4, 6, 8]:
        bst.insert(value)

    # Traversals
    print("In-order Traversal:", bst.inorder_traversal())
    print("Pre-order Traversal:", bst.preorder_traversal())
    print("Post-order Traversal:", bst.postorder_traversal())
    print("Level-order Traversal:", bst.level_order_traversal())

    # Other operations
    print("Search for 4:", bst.search(4) is not None)
    print("Maximum value:", bst.max_value())
    print("Total nodes:", bst.count_nodes())
    print("Height of BST:", bst.height())
    print("Is valid BST:", bst.is_valid_bst())

    # Deletion example
    bst.delete(3)
    print("After deleting 3 (In-order):", bst.inorder_traversal())
