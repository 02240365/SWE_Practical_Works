# Step 1: Define the Node Class

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



# Step 2: Create the LinkedList Class

class LinkedList:
    def __init__(self):
        self.head = None



# Step 3: Implement the Append Method

class Node:
    def __init__(self, data):
        """Initialize a new node with the given data."""
        self.data = data  # Store the data
        self.next = None  # Initialize next as None

class LinkedList:
    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None  # The head of the list is initially None

    def append(self, data):
        """Append a node with the given data to the end of the linked list."""
        new_node = Node(data)  # Create a new node
        if not self.head:  # If the list is empty
            self.head = new_node  # Set head to the new node
            return
        current = self.head  # Start at the head
        while current.next:  # Traverse to the last node
            current = current.next
        current.next = new_node  # Link the new node at the end

    def display(self):
        """Display the contents of the linked list."""
        elements = []  # List to hold the elements
        current = self.head  # Start from the head
        while current:  # Traverse until the end of the list
            elements.append(current.data)  # Collect the data
            current = current.next  # Move to the next node
        print(" -> ".join(map(str, elements)))  # Print the linked list

# Test the append method
ll = LinkedList()  # Create a new linked list
ll.append(1)  # Append 1
ll.append(2)  # Append 2
ll.append(3)  # Append 3

# Display the contents of the linked list
print("Linked list contents:")
ll.display()  # Output: 1 -> 2 -> 3





# Step 4: Implement the Display Method

class LinkedList:
    # ... (previous code)

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

# Test the display method
ll.display()  # Output: 1 -> 2 -> 3



# Step 5: Implement the Insert Method

class Node:
    def __init__(self, data):
        """Initialize a new node with the given data."""
        self.data = data  # Store the data
        self.next = None  # Initialize next as None

class LinkedList:
    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None  # The head of the list is initially None

    def append(self, data):
        """Append a node with the given data to the end of the linked list."""
        new_node = Node(data)  # Create a new node
        if not self.head:  # If the list is empty
            self.head = new_node  # Set head to the new node
            return
        current = self.head  # Start at the head
        while current.next:  # Traverse to the last node
            current = current.next
        current.next = new_node  # Link the new node at the end

    def insert(self, data, position):
        """Insert a node with the given data at a specific position."""
        new_node = Node(data)  # Create a new node
        if position == 0:  # If inserting at the head
            new_node.next = self.head  # Point new node to the current head
            self.head = new_node  # Update head to the new node
            return
        current = self.head  # Start from the head
        for _ in range(position - 1):  # Traverse to the node before the desired position
            if current is None:  # If we reach the end before position
                raise IndexError("Position out of range")
            current = current.next
        new_node.next = current.next  # Link the new node to the next node
        current.next = new_node  # Link the previous node to the new node

    def display(self):
        """Display the contents of the linked list."""
        elements = []  # List to hold the elements
        current = self.head  # Start from the head
        while current:  # Traverse until the end of the list
            elements.append(current.data)  # Collect the data
            current = current.next  # Move to the next node
        print(" -> ".join(map(str, elements)))  # Print the linked list

# Test the LinkedList implementation
ll = LinkedList()  # Create a new linked list
ll.append(1)  # Append 1
ll.append(2)  # Append 2
ll.append(3)  # Append 3

# Display the current linked list contents
print("Before insertion:")
ll.display()  # Expected output: 1 -> 2 -> 3

# Insert 4 at position 1
ll.insert(4, 1)

# Display the updated linked list contents
print("After inserting 4 at position 1:")
ll.display()  # Expected output: 1 -> 4 -> 2 -> 3




# Step 6: Implement the Delete Method

class Node:
    def __init__(self, data):
        """Initialize a new node with the given data."""
        self.data = data  # Store the data
        self.next = None  # Initialize next as None

class LinkedList:
    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None  # The head of the list is initially None

    def append(self, data):
        """Append a node with the given data to the end of the linked list."""
        new_node = Node(data)  # Create a new node
        if not self.head:  # If the list is empty
            self.head = new_node  # Set head to the new node
            return
        current = self.head  # Start at the head
        while current.next:  # Traverse to the last node
            current = current.next
        current.next = new_node  # Link the new node at the end

    def delete(self, data):
        """Delete the first node with the given data."""
        if not self.head:  # If the list is empty
            return
        if self.head.data == data:  # If the head needs to be deleted
            self.head = self.head.next  # Move head to the next node
            return
        current = self.head  # Start from the head
        while current.next:  # Traverse the list
            if current.next.data == data:  # Check if the next node is the one to delete
                current.next = current.next.next  # Bypass the node to delete it
                return
            current = current.next  # Move to the next node

    def display(self):
        """Display the contents of the linked list."""
        elements = []  # List to hold the elements
        current = self.head  # Start from the head
        while current:  # Traverse until the end of the list
            elements.append(current.data)  # Collect the data
            current = current.next  # Move to the next node
        print(" -> ".join(map(str, elements)))  # Print the linked list

# Test the LinkedList implementation
ll = LinkedList()  # Create a new linked list
ll.append(1)  # Append 1
ll.append(2)  # Append 2
ll.append(3)  # Append 3

# Display the current linked list contents
print("Before deletion:")
ll.display()  # Expected output: 1 -> 2 -> 3

# Delete node with value 2
ll.delete(2)

# Display the updated linked list contents
print("After deleting 2:")
ll.display()  # Expected output: 1 -> 3




# Step 7: Implement the Search Method

class Node:
    def __init__(self, data):
        """Initialize a new node with the given data."""
        self.data = data  # Store the data
        self.next = None  # Initialize next as None

class LinkedList:
    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None  # The head of the list is initially None

    def append(self, data):
        """Append a node with the given data to the end of the linked list."""
        new_node = Node(data)  # Create a new node
        if not self.head:  # If the list is empty
            self.head = new_node  # Set head to the new node
            return
        current = self.head  # Start at the head
        while current.next:  # Traverse to the last node
            current = current.next
        current.next = new_node  # Link the new node at the end

    def search(self, data):
        """Search for a node with the given data and return its position."""
        current = self.head  # Start from the head
        position = 0  # Initialize position counter
        while current:  # Traverse the list
            if current.data == data:  # If data matches
                return position  # Return the position
            current = current.next  # Move to the next node
            position += 1  # Increment the position
        return -1  # If not found, return -1

# Test the LinkedList implementation
ll = LinkedList()  # Create a new linked list
ll.append(1)  # Append 1
ll.append(2)  # Append 2
ll.append(3)  # Append 3

# Test the search method
print(ll.search(2))  # Output: 1 (the index of the value 2)
print(ll.search(4))  # Output: -1 (not found)
print(ll.search(1))  # Output: 0 (the index of the value 1)
print(ll.search(3))  # Output: 2 (the index of the value 3)





# Step 8: Implement the Reverse Method

class Node:
    def __init__(self, data):
        """Initialize a new node with the given data."""
        self.data = data  # Store the data
        self.next = None  # Initialize next as None

class LinkedList:
    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None  # The head of the list is initially None

    def append(self, data):
        """Append a node with the given data to the end of the linked list."""
        new_node = Node(data)  # Create a new node
        if not self.head:  # If the list is empty
            self.head = new_node  # Set head to the new node
            return
        current = self.head  # Start at the head
        while current.next:  # Traverse to the last node
            current = current.next
        current.next = new_node  # Link the new node at the end

    def display(self):
        """Display the elements of the linked list."""
        elements = []  # List to store node values
        current = self.head  # Start from the head
        while current:  # Traverse the list
            elements.append(current.data)  # Add node data to the list
            current = current.next  # Move to the next node
        print(" -> ".join(map(str, elements)))  # Print the list

    def reverse(self):
        """Reverse the linked list."""
        prev = None  # Initialize previous node as None
        current = self.head  # Start with the head node
        while current:  # Traverse through the list
            next_node = current.next  # Store the next node
            current.next = prev  # Reverse the current node's pointer
            prev = current  # Move prev to current node
            current = next_node  # Move to the next node
        self.head = prev  # Set the new head to the last processed node

# Test the LinkedList implementation
ll = LinkedList()  # Create a new linked list
ll.append(1)  # Append 1
ll.append(2)  # Append 2
ll.append(3)  # Append 3

print("Original list:")
ll.display()  # Display the original list: 1 -> 2 -> 3

ll.reverse()  # Reverse the linked list

print("Reversed list:")
ll.display()  # Display the reversed list: 3 -> 2 -> 1





#Exercises

# 1.Find Middle Element

def find_middle(self):
    slow = self.head
    fast = self.head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.data if slow else None



# 2.Detect Cycle

def has_cycle(self):
    slow = self.head
    fast = self.head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False




# 3.Remove Duplicates from Unsorted List

def remove_duplicates(self):
    current = self.head
    seen_data = set()  # Set to store seen values
    prev = None
    while current:
        if current.data in seen_data:
            prev.next = current.next  # Remove duplicate node
        else:
            seen_data.add(current.data)
            prev = current
        current = current.next




# 4.Merge Two Sorted Linked Lists
class Node:
    def __init__(self, data):
        """Initialize a new node with the given data."""
        self.data = data  # Store the data
        self.next = None  # Initialize next as None

class LinkedList:
    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None  # The head of the list is initially None

    def append(self, data):
        """Append a node with the given data to the end of the linked list."""
        new_node = Node(data)  # Create a new node
        if not self.head:  # If the list is empty
            self.head = new_node  # Set head to the new node
            return
        current = self.head  # Start at the head
        while current.next:  # Traverse to the last node
            current = current.next
        current.next = new_node  # Link the new node at the end

    def display(self):
        """Display the elements of the linked list."""
        elements = []  # List to store node values
        current = self.head  # Start from the head
        while current:  # Traverse the list
            elements.append(current.data)  # Add node data to the list
            current = current.next  # Move to the next node
        print(" -> ".join(map(str, elements)))  # Print the list

    def find_middle(self):
        """Find the middle element of the linked list."""
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None

    def has_cycle(self):
        """Detect if the linked list has a cycle."""
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:  # Cycle detected
                return True
        return False

    def remove_duplicates(self):
        """Remove duplicates from the linked list."""
        current = self.head
        seen = set()
        prev = None
        while current:
            if current.data in seen:
                prev.next = current.next  # Bypass the current node
            else:
                seen.add(current.data)
                prev = current
            current = current.next

    def merge_sorted(self, other_list):
        """Merge two sorted linked lists into one sorted linked list."""
        merged_list = LinkedList()  # Create a new linked list for merged result
        p1 = self.head
        p2 = other_list.head

        # Creating a dummy node to build upon
        dummy = Node(0)
        current = dummy

        while p1 and p2:
            if p1.data < p2.data:
                current.next = p1  # Link the smaller node
                p1 = p1.next
            else:
                current.next = p2  # Link the smaller node
                p2 = p2.next
            current = current.next  # Move to the next position

        # Add remaining nodes of the lists
        if p1:
            current.next = p1
        elif p2:
            current.next = p2

        merged_list.head = dummy.next  # Skipping the dummy node
        return merged_list


# Testing the functions

# Creating and populating the linked list
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

# Display initial list
print("Initial List:")
ll.display()

# Test finding the middle element
print("\nMiddle element:", ll.find_middle())

# Test cycle detection
print("\nCycle detection (expect False):", ll.has_cycle())

# Test removing duplicates
print("\nRemoving duplicates...")
ll.append(3)  # Adding a duplicate for testing
ll.display()
ll.remove_duplicates()
print("After removing duplicates:")
ll.display()

# Test merging two sorted linked lists
ll2 = LinkedList()
ll2.append(2)
ll2.append(4)
ll2.append(6)
print("\nMerging with another sorted list:")
ll.display()
ll2.display()
merged_list = ll.merge_sorted(ll2)
print("Merged List:")
merged_list.display()
