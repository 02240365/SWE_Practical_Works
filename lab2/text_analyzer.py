# Define the content for the text file
content = """
Python is an interpreted, high-level, general-purpose programming language.
It was created by Guido van Rossum and first released in 1991.
Python's design philosophy emphasizes code readability with the use of significant indentation.
Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.
Python is dynamically typed and garbage-collected.
It supports multiple programming paradigms, including structured (particularly, procedural), object-oriented, and functional programming.
"""

# Create and write to the text file
with open('sample.txt', 'w') as file:
    file.write(content)

print("sample.txt has been created and written to successfully.")


# Step 1: Open and Read a Text File

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

# Test the function
content = read_file('sample.txt')
print(content[:100])  # Print the first 100 characters



# Step 2: Count the Number of Lines

def count_lines(content):
    return len(content.split('\n'))

# Test the function
num_lines = count_lines(content)
print(f"Number of lines: {num_lines}")



# Step 3: Count Words

def count_words(content):
    return len(content.split())

# Test the function
num_words = count_words(content)
print(f"Number of words: {num_words}")



# Step 4: Find the Most Common Word

from collections import Counter

def most_common_word(content):
    words = content.lower().split()
    word_counts = Counter(words)
    return word_counts.most_common(1)[0]

# Test the function
common_word, count = most_common_word(content)
print(f"Most common word: '{common_word}' (appears {count} times)")



# Step 5: Calculate Average Word Length

def average_word_length(content):
    words = content.split()
    total_length = sum(len(word) for word in words)
    return total_length / len(words)

# Test the function
avg_length = average_word_length(content)
print(f"Average word length: {avg_length:.2f} characters")



# Step 6: Combine Everything into a Main Function

def analyze_text(filename):
    content = read_file(filename)
    
    num_lines = count_lines(content)
    num_words = count_words(content)
    common_word, count = most_common_word(content)
    avg_length = average_word_length(content)
    
    print(f"File: {filename}")
    print(f"Number of lines: {num_lines}")
    print(f"Number of words: {num_words}")
    print(f"Most common word: '{common_word}' (appears {count} times)")
    print(f"Average word length: {avg_length:.2f} characters")

# Run the analysis
analyze_text('sample.txt')





# Exercises

# 1.Count the number of unique words in the text.

def count_unique_words(content):
    words = set(content.lower().split())
    return len(words)

# Add to analyze_text
num_unique_words = count_unique_words(content)
print(f"Number of unique words: {num_unique_words}")


# 2.Find the longest word in the text.
def longest_word(content):
    words = content.split()
    return max(words, key=len)

# Add to analyze_text
long_word = longest_word(content)
print(f"Longest word: '{long_word}'")


# 3.Count the occurrences of a specific word (case-insensitive).

def count_specific_word(content, word):
    words = content.lower().split()
    return words.count(word.lower())

# Add to analyze_text
specific_word = 'your_word_here'  # Replace with the word you want to search
specific_word_count = count_specific_word(content, specific_word)
print(f"Occurrences of '{specific_word}': {specific_word_count}")


# 4.Calculate the percentage of words that are longer than the average word length.

def percentage_longer_than_avg(content):
    words = content.split()
    avg_length = average_word_length(content)
    long_words = [word for word in words if len(word) > avg_length]
    return (len(long_words) / len(words)) * 100

# Add to analyze_text
percentage_long = percentage_longer_than_avg(content)
print(f"Percentage of words longer than average:")
