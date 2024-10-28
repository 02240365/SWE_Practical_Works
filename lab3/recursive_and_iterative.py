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

# 1.Returning a list of Fibonacci numbers up to n, instead of just the nth number.

def fibonacci_list(n):
    if n <= 0:
        return [0]
    sequence = [0, 1]
    for _ in range(2, n + 1):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

# Test the function
print(f"Fibonacci sequence up to F(20): {fibonacci_list(20)}")




# 2.Finding the index of the first Fibonacci number that exceeds a given value.

def find_fibonacci_exceeding(value):
    a, b = 0, 1
    index = 1
    while b <= value:
        a, b = b, a + b
        index += 1
    return index

# Test the function
value = 67
print(f"The first Fibonacci number greater than {value} is at index {find_fibonacci_exceeding(value)}")




# 3.Determining if a given number is a Fibonacci number.

def is_fibonacci_number(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    return b == num or num == 0

# Test the function
test_num = 19
print(f"{test_num} is a Fibonacci number: {is_fibonacci_number(test_num)}")




# 4.Calculating the ratio between consecutive Fibonacci numbers and observe how it approaches the golden ratio.

def fibonacci_ratios(limit):
    a, b = 0, 1
    ratios = []
    for _ in range(2, limit + 1):
        ratio = b / a if a != 0 else 0
        ratios.append(ratio)
        a, b = b, a + b
    return ratios

# Test the function
limit = 10
ratios = fibonacci_ratios(limit)
print("Ratios between consecutive Fibonacci numbers:", ratios)






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