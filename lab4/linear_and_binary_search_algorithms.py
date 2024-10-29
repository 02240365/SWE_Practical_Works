# Step 1: Implement Linear Search

def linear_search(arr, target):
    indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)  # Collect all indices where the target is found
    return indices if indices else -1  # Return indices or -1 if not found

# Test the function
test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
result = linear_search(test_list, 6)
print(f"Linear Search: Indices of 6 are {result}")



# Step 2: Implement Binary Search

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Return the index if the target is found
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Return -1 if the target is not in the list

# Test the function
test_list_sorted = sorted(test_list)
result = binary_search(test_list_sorted, 6)
print(f"Binary Search: Index of 6 in sorted list is {result}")



# Step 3: Compare Performance

import time

def compare_search_algorithms(arr, target):
    # Linear Search
    start_time = time.time()
    linear_result = linear_search(arr, target)
    linear_time = time.time() - start_time

    # Binary Search (on sorted array)
    arr_sorted = sorted(arr)
    start_time = time.time()
    binary_result = binary_search(arr_sorted, target)
    binary_time = time.time() - start_time

    print(f"Linear Search: Found at indices {linear_result}, Time: {linear_time:.6f} seconds")
    print(f"Binary Search: Found at index {binary_result}, Time: {binary_time:.6f} seconds")

# Test with a larger list
large_list = list(range(10000))
compare_search_algorithms(large_list, 8888)




# Step 4: Implement Recursive Binary Search

def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

# Test the recursive function
result = binary_search_recursive(test_list_sorted, 6, 0, len(test_list_sorted) - 1)
print(f"Recursive Binary Search: Index of 6 in sorted list is {result}")




# Step 5: Create a Main Function

def main():
    # Create a list of 20 random integers between 1 and 100
    import random
    test_list = [random.randint(1, 100) for _ in range(20)]
    
    print("Original list:", test_list)
    print("Sorted list:", sorted(test_list))
    
    target = random.choice(test_list)  # Choose a random target from the list
    print(f"\nSearching for: {target}")
    
    # Linear Search
    result = linear_search(test_list, target)
    print(f"Linear Search: Found at indices {result}")
    
    # Binary Search (iterative)
    sorted_list = sorted(test_list)
    result = binary_search(sorted_list, target)
    print(f"Binary Search (iterative): Found at index {result}")
    
    # Binary Search (recursive)
    result = binary_search_recursive(sorted_list, target, 0, len(sorted_list) - 1)
    print(f"Binary Search (recursive): Found at index {result}")
    
    # Compare performance
    print("\nPerformance Comparison:")
    compare_search_algorithms(list(range(100000)), 99999)

if __name__ == "__main__":
    main()





# Exercises

# 1.Modify the Linear Search Function to Return All Indices of the Target

def linear_search_all_indices(arr, target):
    indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)
    return indices if indices else -1

# Test the modified function
test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
result = linear_search_all_indices(test_list, 5)
print(f"Linear Search (All Indices): Indices of 5 are {result}")



# 2.Binary Search Insertion Point

def binary_search_insertion_point(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

# Test the function
sorted_list = sorted(test_list)
insertion_point = binary_search_insertion_point(sorted_list, 7)
print(f"Insertion Point: Target 7 should be inserted at index {insertion_point}")



# 3.Count Comparisons in Each Search Algorithm

def linear_search_with_count(arr, target):
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons
    return -1, comparisons

def binary_search_with_count(arr, target):
    left, right = 0, len(arr) - 1
    comparisons = 0
    while left <= right:
        comparisons += 1
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1, comparisons

# Test comparison counting functions
target = 6
index, comparisons = linear_search_with_count(test_list, target)
print(f"Linear Search: Found {target} at index {index} with {comparisons} comparisons")

sorted_list = sorted(test_list)
index, comparisons = binary_search_with_count(sorted_list, target)
print(f"Binary Search: Found {target} at index {index} with {comparisons} comparisons")




# 4.Implement a Jump Search Algorithm and Compare Performance

import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    # Jump until we find a block where target may reside
    while arr[min(step, n)-1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    
    # Linear search within the identified block
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    return -1

# Test the Jump Search function
large_sorted_list = list(range(10000))
target = 8888

result = jump_search(large_sorted_list, target)
print(f"Jump Search: Index of {target} is {result}")

# Compare performance with other search algorithms
compare_search_algorithms(large_sorted_list, target)
