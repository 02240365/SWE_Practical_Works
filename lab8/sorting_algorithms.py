# Step 1: Implement Bubble Sort

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Test the function
test_arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(test_arr.copy())
print("Bubble Sort Result:", sorted_arr)



# Step 2: Implement Merge Sort

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Test the function
test_arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = merge_sort(test_arr)
print("Merge Sort Result:", sorted_arr)




# Step 3: Implement Quick Sort

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Test the function
test_arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = quick_sort(test_arr)
print("Quick Sort Result:", sorted_arr)





# Step 4: Compare Performance

import time
import random

def compare_sorting_algorithms(arr):
    algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort)
    ]
    
    for name, func in algorithms:
        arr_copy = arr.copy()
        start_time = time.time()
        func(arr_copy)
        end_time = time.time()
        print(f"{name} took {end_time - start_time:.6f} seconds")

# Generate a large random array
large_arr = [random.randint(1, 1000) for _ in range(1000)]

# Compare the algorithms
compare_sorting_algorithms(large_arr)





# Exercises 

# 1.Implement an in-place version of Quick Sort

def quick_sort_in_place(arr, low=0, high=None):
    """In-place Quick Sort implementation."""
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort_in_place(arr, low, pivot_index - 1)
        quick_sort_in_place(arr, pivot_index + 1, high)

def partition(arr, low, high):
    """Helper function for in-place Quick Sort to partition the array."""
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Test in-place Quick Sort
in_place_test_arr = test_arr.copy()
quick_sort_in_place(in_place_test_arr)
print("In-place Quick Sort Result:", in_place_test_arr)





# 2.Modify Bubble Sort to stop early if the list becomes sorted

def optimized_bubble_sort(arr):
    """Optimized Bubble Sort that stops early if the array is sorted."""
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # If no swaps were made, the list is already sorted
            break
    return arr

# Test optimized Bubble Sort
print("Optimized Bubble Sort Result:", optimized_bubble_sort(test_arr.copy()))





# 3.Hybrid Sort (Merge Sort + Insertion Sort for small subarrays)

def insertion_sort(arr):
    """Helper function to perform Insertion Sort on a small array."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def hybrid_merge_sort(arr, threshold=10):
    """Hybrid Merge Sort that uses Insertion Sort for small subarrays."""
    if len(arr) <= threshold:
        return insertion_sort(arr)
    
    mid = len(arr) // 2
    left = hybrid_merge_sort(arr[:mid], threshold)
    right = hybrid_merge_sort(arr[mid:], threshold)
    
    return merge(left, right)

# Test hybrid Merge Sort
print("Hybrid Merge Sort Result:", hybrid_merge_sort(test_arr.copy()))





# 4.Visualization of Sorting Algorithms using Matplotlib

import matplotlib.pyplot as plt
import time

def visualize_sorting_algorithm(algorithm, arr):
    """Function to visualize the sorting algorithm."""
    fig, ax = plt.subplots()
    ax.set_title(f"Visualizing {algorithm.__name__}")
    bar_rects = ax.bar(range(len(arr)), arr, align="edge", color="skyblue")

    def update(arr, rects):
        for rect, val in zip(rects, arr):
            rect.set_height(val)
        plt.pause(0.05)  # Pause for a moment to see the sorting progress

    # Copy the array and sort it using the provided algorithm
    arr_copy = arr.copy()
    n = len(arr_copy)
    
    # Using Bubble Sort algorithm for visualization
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                swapped = True
                update(arr_copy, bar_rects)
        if not swapped:
            break

    plt.show()

# Test visualization
test_arr = [64, 34, 25, 12, 22, 11, 90]
visualize_sorting_algorithm(bubble_sort, test_arr.copy())
