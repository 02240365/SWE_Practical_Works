# Sorting Algorithms 

This practical implements three classic sorting algorithms: **Bubble Sort**, **Merge Sort**, and **Quick Sort** in Python. Additionally, it includes optimized variations, a hybrid sorting method, and visualizations to help understand the mechanics of each algorithm. By comparing the performance of these algorithms, this project demonstrates the advantages and disadvantages of each approach in terms of time complexity and efficiency.

## Features

1. **Bubble Sort**: A simple comparison-based algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
   - Optimized version included: stops early if the array becomes sorted before all passes are complete.

2. **Merge Sort**: A divide-and-conquer algorithm that recursively splits the array in half, sorts each half, and then merges the sorted halves.
   - Includes a **Hybrid Merge Sort** that switches to **Insertion Sort** for small subarrays, enhancing performance for smaller inputs.

3. **Quick Sort**: Another divide-and-conquer algorithm that partitions the array around a pivot element, then recursively sorts the subarrays.
   - In-place version included, which reduces memory usage by sorting without creating additional arrays.

4. **Algorithm Visualization**: Uses **Matplotlib** to visually display the sorting process for Bubble Sort, helping illustrate how sorting algorithms work step-by-step.

