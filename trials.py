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
    pass  # TODO: replace this line with your code


def snake_to_camel(string):
    pass  # TODO: replace this line with your code


def longest_word_length(words):
    pass  # TODO: replace this line with your code


def truncate(string):
    pass  # TODO: replace this line with your code


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code
