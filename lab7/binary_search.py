# Step 1: Define the Node Class

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



# Step 2: Implement the Binary Search Tree Class

class BinarySearchTree:
    def __init__(self):
        self.root = None



# Step 3: Implement the Insertion Method

class Node:
    """Class to represent a node in a binary search tree."""
    def __init__(self, value):
        self.value = value  # Store the node's value
        self.left = None    # Initialize left child as None
        self.right = None   # Initialize right child as None


class BinarySearchTree:
    """Class to represent a binary search tree."""
    def __init__(self):
        self.root = None  # The root of the BST is initially None

    def insert(self, value):
        """Insert a new value into the binary search tree."""
        if not self.root:
            self.root = Node(value)  # If the tree is empty, set the root
        else:
            self._insert_recursive(self.root, value)  # Otherwise, insert recursively

    def _insert_recursive(self, node, value):
        """Helper method to insert a value recursively."""
        if value < node.value:  # If the value is less, go left
            if node.left is None:  # If there's no left child, insert here
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)  # Recur left
        else:  # If the value is greater or equal, go right
            if node.right is None:  # If there's no right child, insert here
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)  # Recur right


# Test insertion
bst = BinarySearchTree()
for value in [5, 3, 7, 2, 4, 6, 8]:
    bst.insert(value)

# Function to print the tree in-order for verification
def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)  # Visit left subtree
        print(node.value, end=' ')  # Print the value
        in_order_traversal(node.right)  # Visit right subtree

print("In-order traversal of the BST:")
in_order_traversal(bst.root)  # Should print: 2 3 4 5 6 7 8




# Step 4: Implement the Search Method

class Node:
    """Class to represent a node in a binary search tree."""
    def __init__(self, value):
        self.value = value  # Store the node's value
        self.left = None    # Initialize left child as None
        self.right = None   # Initialize right child as None


class BinarySearchTree:
    """Class to represent a binary search tree."""
    def __init__(self):
        self.root = None  # The root of the BST is initially None

    def insert(self, value):
        """Insert a new value into the binary search tree."""
        if not self.root:
            self.root = Node(value)  # If the tree is empty, set the root
        else:
            self._insert_recursive(self.root, value)  # Otherwise, insert recursively

    def _insert_recursive(self, node, value):
        """Helper method to insert a value recursively."""
        if value < node.value:  # If the value is less, go left
            if node.left is None:  # If there's no left child, insert here
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)  # Recur left
        else:  # If the value is greater or equal, go right
            if node.right is None:  # If there's no right child, insert here
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)  # Recur right

    def search(self, value):
        """Search for a value in the binary search tree."""
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """Helper method to search for a value recursively."""
        if node is None:  # Base case: node is not found
            return None
        if node.value == value:  # Value found
            return node
        if value < node.value:  # Search left
            return self._search_recursive(node.left, value)
        else:  # Search right
            return self._search_recursive(node.right, value)


# Test the Binary Search Tree with insertion and searching
bst = BinarySearchTree()
for value in [5, 3, 7, 2, 4, 6, 8]:
    bst.insert(value)

# Test search
found_node = bst.search(4)  # Should return the Node with value 4
if found_node:
    print(f"Found: {found_node.value}")  # Should print: Found: 4
else:
    print("Not found: 4")

not_found_node = bst.search(9)  # Should return None
if not_found_node:
    print(f"Found: {not_found_node.value}")
else:
    print("Not found: 9")  # Should print: Not found: 9




# Step 5: Implement Traversal Methods

class Node:
    """Class to represent a node in a binary search tree."""
    def __init__(self, value):
        self.value = value  # Store the node's value
        self.left = None    # Initialize left child as None
        self.right = None   # Initialize right child as None


class BinarySearchTree:
    """Class to represent a binary search tree."""
    def __init__(self):
        self.root = None  # The root of the BST is initially None

    def insert(self, value):
        """Insert a new value into the binary search tree."""
        if not self.root:
            self.root = Node(value)  # If the tree is empty, set the root
        else:
            self._insert_recursive(self.root, value)  # Otherwise, insert recursively

    def _insert_recursive(self, node, value):
        """Helper method to insert a value recursively."""
        if value < node.value:  # If the value is less, go left
            if node.left is None:  # If there's no left child, insert here
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)  # Recur left
        else:  # If the value is greater or equal, go right
            if node.right is None:  # If there's no right child, insert here
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)  # Recur right

    def search(self, value):
        """Search for a value in the binary search tree."""
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """Helper method to search for a value recursively."""
        if node is None:  # Base case: node is not found
            return None
        if node.value == value:  # Value found
            return node
        if value < node.value:  # Search left
            return self._search_recursive(node.left, value)
        else:  # Search right
            return self._search_recursive(node.right, value)

    def inorder_traversal(self):
        """Perform an in-order traversal of the tree."""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        """Helper method for in-order traversal."""
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

    def preorder_traversal(self):
        """Perform a pre-order traversal of the tree."""
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node, result):
        """Helper method for pre-order traversal."""
        if node:
            result.append(node.value)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    def postorder_traversal(self):
        """Perform a post-order traversal of the tree."""
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node, result):
        """Helper method for post-order traversal."""
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)


# Test the Binary Search Tree with insertion and traversals
bst = BinarySearchTree()
for value in [5, 3, 7, 2, 4, 6, 8]:
    bst.insert(value)

# Test traversals
print("In-order:", bst.inorder_traversal())   # Should print: In-order: [2, 3, 4, 5, 6, 7, 8]
print("Pre-order:", bst.preorder_traversal()) # Should print: Pre-order: [5, 3, 2, 4, 7, 6, 8]
print("Post-order:", bst.postorder_traversal()) # Should print: Post-order: [2, 4, 3, 6, 8, 7, 5]





# Step 6: Implement the Deletion Method

class Node:
    """Class to represent a node in a binary search tree."""
    def __init__(self, value):
        self.value = value  # Store the node's value
        self.left = None    # Initialize left child as None
        self.right = None   # Initialize right child as None


class BinarySearchTree:
    """Class to represent a binary search tree."""
    def __init__(self):
        self.root = None  # The root of the BST is initially None

    def insert(self, value):
        """Insert a new value into the binary search tree."""
        if not self.root:
            self.root = Node(value)  # If the tree is empty, set the root
        else:
            self._insert_recursive(self.root, value)  # Otherwise, insert recursively

    def _insert_recursive(self, node, value):
        """Helper method to insert a value recursively."""
        if value < node.value:  # If the value is less, go left
            if node.left is None:  # If there's no left child, insert here
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)  # Recur left
        else:  # If the value is greater or equal, go right
            if node.right is None:  # If there's no right child, insert here
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)  # Recur right

    def search(self, value):
        """Search for a value in the binary search tree."""
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """Helper method to search for a value recursively."""
        if node is None:  # Base case: node is not found
            return None
        if node.value == value:  # Value found
            return node
        if value < node.value:  # Search left
            return self._search_recursive(node.left, value)
        else:  # Search right
            return self._search_recursive(node.right, value)

    def inorder_traversal(self):
        """Perform an in-order traversal of the tree."""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        """Helper method for in-order traversal."""
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

    def preorder_traversal(self):
        """Perform a pre-order traversal of the tree."""
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node, result):
        """Helper method for pre-order traversal."""
        if node:
            result.append(node.value)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    def postorder_traversal(self):
        """Perform a post-order traversal of the tree."""
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node, result):
        """Helper method for post-order traversal."""
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)

    def delete(self, value):
        """Delete a value from the binary search tree."""
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        """Helper method to delete a value recursively."""
        if node is None:
            return node

        if value < node.value:  # Value is less than current node, go left
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:  # Value is greater, go right
            node.right = self._delete_recursive(node.right, value)
        else:
            # Node with only one child or no child
            if node.left is None:  # No left child
                return node.right
            elif node.right is None:  # No right child
                return node.left

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            node.value = self._min_value(node.right)
            node.right = self._delete_recursive(node.right, node.value)

        return node

    def _min_value(self, node):
        """Get the minimum value node in a subtree."""
        current = node
        while current.left is not None:  # Traverse left to find the smallest value
            current = current.left
        return current.value  # Return the smallest value


# Test the Binary Search Tree with insertion, deletion, and traversals
bst = BinarySearchTree()
for value in [5, 3, 7, 2, 4, 6, 8]:
    bst.insert(value)

print("Initial In-order:", bst.inorder_traversal())  # Should print: [2, 3, 4, 5, 6, 7, 8]

# Test deletion
bst.delete(3)
print("After deleting 3:", bst.inorder_traversal())  # Should print: [2, 4, 5, 6, 7, 8]

bst.delete(5)
print("After deleting 5:", bst.inorder_traversal())  # Should print: [2, 4, 6, 7, 8]

bst.delete(7)
print("After deleting 7:", bst.inorder_traversal())  # Should print: [2, 4, 6, 8]





# Exercises

class Node:
    """Class to represent a node in the binary search tree."""
    def __init__(self, value):
        self.value = value  # Store the node's value
        self.left = None    # Initialize left child as None
        self.right = None   # Initialize right child as None


class BinarySearchTree:
    """Class to represent a binary search tree."""
    def __init__(self):
        self.root = None  # The root of the BST is initially None

    def insert(self, value):
        """Insert a new value into the binary search tree."""
        if not self.root:
            self.root = Node(value)  # If the tree is empty, set the root
        else:
            self._insert_recursive(self.root, value)  # Otherwise, insert recursively

    def _insert_recursive(self, node, value):
        """Helper method to insert a value recursively."""
        if value < node.value:  # If the value is less, go left
            if node.left is None:  # If there's no left child, insert here
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)  # Recur left
        else:  # If the value is greater or equal, go right
            if node.right is None:  # If there's no right child, insert here
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)  # Recur right

    def search(self, value):
        """Search for a value in the binary search tree."""
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """Helper method to search for a value recursively."""
        if node is None:  # Base case: node is not found
            return None
        if node.value == value:  # Value found
            return node
        if value < node.value:  # Search left
            return self._search_recursive(node.left, value)
        else:  # Search right
            return self._search_recursive(node.right, value)

    def inorder_traversal(self):
        """Perform an in-order traversal of the tree."""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        """Helper method for in-order traversal."""
        if node:
            self._inorder_recursive(node.left, result)  # Visit left subtree
            result.append(node.value)  # Visit node
            self._inorder_recursive(node.right, result)  # Visit right subtree

    def preorder_traversal(self):
        """Perform a pre-order traversal of the tree."""
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node, result):
        """Helper method for pre-order traversal."""
        if node:
            result.append(node.value)  # Visit node
            self._preorder_recursive(node.left, result)  # Visit left subtree
            self._preorder_recursive(node.right, result)  # Visit right subtree

    def postorder_traversal(self):
        """Perform a post-order traversal of the tree."""
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node, result):
        """Helper method for post-order traversal."""
        if node:
            self._postorder_recursive(node.left, result)  # Visit left subtree
            self._postorder_recursive(node.right, result)  # Visit right subtree
            result.append(node.value)  # Visit node

    def delete(self, value):
        """Delete a value from the binary search tree."""
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        """Helper method to delete a value recursively."""
        if node is None:  # Base case: empty node
            return node

        if value < node.value:  # Value is less than current node, go left
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:  # Value is greater, go right
            node.right = self._delete_recursive(node.right, value)
        else:
            # Node with only one child or no child
            if node.left is None:  # No left child
                return node.right
            elif node.right is None:  # No right child
                return node.left

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            node.value = self._min_value(node.right)
            node.right = self._delete_recursive(node.right, node.value)

        return node

    def _min_value(self, node):
        """Get the minimum value node in a subtree."""
        current = node
        while current.left is not None:  # Traverse left to find the smallest value
            current = current.left
        return current.value  # Return the smallest value



# 1.Maximum value in the BST

    def max_value(self):
        """Find the maximum value in the BST."""
        if self.root is None:
            return None
        current = self.root
        while current.right is not None:  # Traverse right to find the largest value
            current = current.right
        return current.value  # Return the largest value




# 2.Count the total number of nodes in the BST

    def count_nodes(self):
        """Count the total number of nodes in the BST."""
        return self._count_nodes_recursive(self.root)

    def _count_nodes_recursive(self, node):
        """Helper method to count nodes recursively."""
        if node is None:  # Base case: empty node
            return 0
        return 1 + self._count_nodes_recursive(node.left) + self._count_nodes_recursive(node.right)  # Count self + left + right




# 3. Implement level-order traversal for the BST

    def level_order_traversal(self):
        """Perform a level-order traversal (breadth-first search)."""
        result = []
        if not self.root:  # If the tree is empty
            return result

        queue = [self.root]  # Initialize queue with the root node

        while queue:
            current = queue.pop(0)  # Dequeue the front node
            result.append(current.value)  # Process the current node
            if current.left:  # If there is a left child, enqueue it
                queue.append(current.left)
            if current.right:  # If there is a right child, enqueue it
                queue.append(current.right)

        return result  # Return the list of values in level order
    



# 4.Find the height of the BST

    def height(self):
        """Calculate the height of the BST."""
        return self._height_recursive(self.root)

    def _height_recursive(self, node):
        """Helper method to calculate height recursively."""
        if node is None:  # Base case: empty node
            return -1  # Height of an empty tree is -1
        left_height = self._height_recursive(node.left)  # Height of left subtree
        right_height = self._height_recursive(node.right)  # Height of right subtree
        return 1 + max(left_height, right_height)  # Height of the tree is max of both heights + 1

    def is_valid_bst(self):
        """Check if the tree is a valid binary search tree."""
        return self._is_valid_bst_recursive(self.root, float('-inf'), float('inf'))

    def _is_valid_bst_recursive(self, node, min_value, max_value):
        """Helper method to validate the BST recursively."""
        if node is None:  # Base case: empty node
            return True
        if node.value <= min_value or node.value >= max_value:  # Check BST property
            return False
        return (self._is_valid_bst_recursive(node.left, min_value, node.value) and  # Validate left subtree
                self._is_valid_bst_recursive(node.right, node.value, max_value))  # Validate right subtree


# 5.Check if the tree is a valid BST

if __name__ == "__main__":
    bst = BinarySearchTree()
    # Inserting values into the BST
    for value in [5, 3, 7, 2, 4, 6, 8]:
        bst.insert(value)

    # Test insertion
    print("In-order Traversal:", bst.inorder_traversal())  # Should print: [2, 3, 4, 5, 6, 7, 8]
    print("Pre-order Traversal:", bst.preorder_traversal())  # Should print: [5, 3, 2, 4, 7, 6, 8]
    print("Post-order Traversal:", bst.postorder_traversal())  # Should print: [2, 4, 3, 6, 8, 7, 5]

    # Test search
    print("Search for 4:", bst.search(4) is not None)  # Should return True
    print("Search for 9:", bst.search(9) is None)  # Should return True

    # Test maximum value
    print("Maximum value:", bst.max_value())  # Should return 8

    # Test node count
    print("Total nodes:", bst.count_nodes())  # Should return 7

    # Test level-order traversal
    print("Level-order Traversal:", bst.level_order_traversal())  # Should print: [5, 3, 7, 2, 4, 6, 8]

    # Test height
    print("Height of BST:", bst.height())  # Should return 2

    # Test if the tree is a valid BST
    print("Is valid BST:", bst.is_valid_bst())  # Should return True

    # Test deletion
    bst.delete(3)
    print("After deleting 3 (In-order):", bst.inorder_traversal())  # Should print: [2, 4, 5, 6, 7, 8]
