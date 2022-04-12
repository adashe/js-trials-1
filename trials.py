"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    """print all items in list"""

    for item in items:
        print(item)

# output_all_items([1, "hello", True])

def get_all_evens(nums):
    """return a list of even numbers"""

    new_nums = []
    for num in nums:
        if num % 2 == 0:
            new_nums.append(num)
    return new_nums

# print(get_all_evens([7, 8, 10, 1, 2, 2]))

def get_odd_indices(items):
    """return all elements at odd numbered indices"""

    result = []
    for i, item in enumerate(items):
        if i % 2 != 0:
            result.append(item)

    return result

# print(get_odd_indices([1, 'hello', True, 500]))

def print_as_numbered_list(items):
    """Given an array, output a numbered list"""

    for i, item in enumerate(items):
        print(f"{i + 1}. {item}")

# print_as_numbered_list([1, 'hello', True])

def get_range(start, stop):
    """Return an array of numbers in a certain range"""
    result = []

    for i in range(start, stop):
        result.append(i)

    return result

# print(get_range(0, 5))
# print(get_range(1, 3))

def censor_vowels(word):
    """Given a string, returns a string where vowels are replaced with '*'."""
    chars = []

    for letter in word:
        if letter in 'aeiou':
            chars.append('*')
        else:
            chars.append(letter)

    return ''.join(chars)

# print(censor_vowels('hello world'))

def snake_to_camel(string):
    """Given a string in snake case, return a string in upper camel case."""
    camel_case = []

    for word in string.split('_'):
        camel_case.append(f'{word[0].upper()}{word[1:]}')

    return ''.join(camel_case)

# print(snake_to_camel('hello_world'))

def longest_word_length(words):
    """Return the length of the longest word in the given array of words."""
    longest = len(words[0])

    for word in words:
        if longest < len(word):
            longest = len(word)

    return longest

# print(longest_word_length(['hello', 'world']))
# print(longest_word_length(['jellyfish', 'zebra']))

def truncate(string):
    """Truncate repeating characters into one character."""
    result = []

    for char in string:
        if len(result) == 0 or char != result[-1]:
            result.append(char)
    
    return ''.join(result)

# print(truncate('aaaabbbbcccca'))
# print(truncate('hi***!!!! wooow'))

def has_balanced_parens(string):
    """Return true if all parentheses in a given string are balanced."""
    parens = 0

    for char in string:
        if char == '(':
            parens += 1
        elif char == ')':
            parens -= 1
        
        if parens < 0:
            return False

    return parens == 0

# print(has_balanced_parens('()'))
# print(has_balanced_parens('((This) (is) (good))'))
# print(has_balanced_parens('(Oh no!)('))

def compress(string):
    """Return a compressed version of the given string."""
    compressed = []
    
    curr_char = ''
    char_count = 0

    for char in string:
        if char != curr_char:
            compressed.append(curr_char)
        
            if char_count > 1:
                compressed.append(str(char_count))

            curr_char = char
            char_count = 0
        
        char_count += 1

    compressed.append(curr_char)

    if char_count > 1:
        compressed.append(str(char_count))

    return ''.join(compressed)

# print(compress('abc'))
# print(compress('Hello, world! Cows go moooo...'))
