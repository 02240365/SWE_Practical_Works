# Step 1: Implementing a Recursive Fibonacci Generator

def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Test the function
for i in range(10):
    print(f"F({i}) = {fibonacci_recursive(i)}")



# Step 2: Implementing an Iterative Fibonacci Generator

def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Test the function
for i in range(10):
    print(f"F({i}) = {fibonacci_iterative(i)}")



# Step 3: Comparing Performance

import time

def measure_time(func, n):
    start = time.time()
    result = func(n)
    end = time.time()
    return result, end - start

# Test both functions and compare their execution times
n = 30
recursive_result, recursive_time = measure_time(fibonacci_recursive, n)
iterative_result, iterative_time = measure_time(fibonacci_iterative, n)

print(f"Recursive: F({n}) = {recursive_result}, Time: {recursive_time:.6f} seconds")
print(f"Iterative: F({n}) = {iterative_result}, Time: {iterative_time:.6f} seconds")


# Step 4: Implementing a Generator Function for Fibonacci Sequence

def fibonacci_generator(limit):
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1

# Test the generator
for i, fib in enumerate(fibonacci_generator(10)):
    print(f"F({i}) = {fib}")


# Step 5: Implementing Memoization for Recursive Fibonacci

def fibonacci_memoized(n, memo={}):
    # Check if the result is already in the memo dictionary
    if n in memo:
        return memo[n]
    # Base case: return n for F(0) and F(1)
    if n <= 1:
        return n
    # Store the result in the memo dictionary to avoid redundant calculations
    memo[n] = fibonacci_memoized(n-1, memo) + fibonacci_memoized(n-2, memo)
    return memo[n]

# Test the memoized function
for i in range(10):
    print(f"F({i}) = {fibonacci_memoized(i)}")

# Compare performance with the original recursive function
n = 30
memoized_result, memoized_time = measure_time(fibonacci_memoized, n)
print(f"Memoized: F({n}) = {memoized_result}, Time: {memoized_time:.6f} seconds")



# Exercises

# 1.Modify the iterative function to return a list of Fibonacci numbers up to n:

def fibonacci_iterative_list(n):
    fib_list = []
    if n >= 0:
        fib_list.append(0)
    if n >= 1:
        fib_list.append(1)
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
        fib_list.append(b)
    return fib_list

# Test the modified function
print(fibonacci_iterative_list(10))


# 2.Implement a function that finds the index of the first Fibonacci number that exceeds a given value:

def first_fib_exceeding(value):
    a, b = 0, 1
    index = 0
    while a <= value:
        a, b = b, a + b
        index += 1
    return index

# Test the function
print(first_fib_exceeding(21))  # Should return 8, since F(8) = 21 




# 3.Create a function that determines if a given number is a Fibonacci number:

def is_fibonacci(num):
    if num < 0:
        return False
    
    # A number is Fibonacci if one of these expressions is a perfect square
    def is_perfect_square(x):
        s = int(x**0.5)
        return s * s == x
    
    return is_perfect_square(5 * num * num + 4) or is_perfect_square(5 * num * num - 4)

# Test the function
print(is_fibonacci(21))  # True
print(is_fibonacci(22))  # False



# 4.Implement a function that calculates the ratio between consecutive Fibonacci numbers and observe how it approaches the golden ratio:

def fibonacci_ratio(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return b / a

# Test the function
for i in range(10, 20):
    print(f"Fibonacci ratio at {i}: {fibonacci_ratio(i)}")




# Discussion Questions

"""
1.What are the advantages and disadvantages of the recursive approach compared to the iterative approach?
Answer:
The recursive approach has the advantage of being more intuitive and easier to understand, as it directly follows the mathematical definition of the Fibonacci sequence. However, it has the disadvantage of being less efficient due to the repeated computation of the same subproblems, leading to exponential time complexity.

The iterative approach, on the other hand, has the advantage of being more efficient with a linear time complexity, but it can be more difficult to understand and implement.


2.How does memoization improve the performance of the recursive function? Are there any drawbacks?
Answer:
Memoization improves the performance of the recursive function by storing the results of expensive function calls and reusing them when the same inputs occur again. This avoids the repeated computation of the same subproblems, reducing the time complexity from exponential to linear.

However, memoization has the drawback of increasing the space complexity, as it requires additional memory to store the cached results.


3.In what scenarios might you prefer to use a generator function over other implementations?
Answer:
You might prefer to use a generator function when working with large datasets or infinite sequences, as it allows for efficient iteration without storing the entire sequence in memory. This is particularly useful when working with Fibonacci numbers, as the sequence grows rapidly.


4.How does the space complexity differ between these implementations?
Answer:
The recursive implementation has a high space complexity due to the recursive call stack, which grows with the input size.

The iterative implementation has a low space complexity, as it only requires a constant amount of memory to store the current and previous Fibonacci numbers.

The generator implementation has a low space complexity, as it only stores the current and previous Fibonacci numbers, and yields each number on demand.

The memoized implementation has a high space complexity, as it stores the cached results of all previous function calls. However, this is a trade-off for the improved time complexity."""