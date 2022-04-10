"""Dictionaries Practice

**IMPORTANT:** These problems are meant to be solved using
dictionaries and sets.
"""


def without_duplicates(words):
    """Given a list of words, return list with duplicates removed.

    For example:

        >>> no_dupes = without_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"])

        >>> isinstance(no_dupes, list)
        True

        >>> sorted(without_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(without_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

        An empty list should return an empty list:

        >>> sorted(without_duplicates(
        ...     []))
        []

    The function should work for a list containing integers:

        >>> sorted(without_duplicates([111111, 2, 33333, 2]))
        [2, 33333, 111111]

    The function should return a variable of type list:
        >>> type(without_duplicates([111111, 2, 33333, 2]))
        <class 'list'>
    """

    # Generate a set and then convert to a list
    no_duplicates = list(set(words))

    return no_duplicates


def find_unique_common_items(items1, items2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a set of the *unique* common items
    shared between the lists.

    **IMPORTANT**: you may not use `'if ___ in ___``
    or the method `list.index()`.

    This should return a set:

        >>> unique_common_items = find_unique_common_items([1, 2, 3, 4], [2, 1])
        >>> isinstance(unique_common_items, set)
        True

    This should find [1, 2]:

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [2, 1]))
        [1, 2]

    However, now we only want unique items, so for these lists,
    don't show more than 1 or 2 once:

        >>> sorted(find_unique_common_items([3, 2, 1], [1, 1, 2, 2]))
        [1, 2]

    The elements should not be treated as duplicates if they are
    different data types:

        >>> sorted(find_unique_common_items(["2", "1", 2], [2, 1]))
        [2]
    """

    # Find the intersection of two sets
    unique_common_words = set(items1) & set(items2)

    return unique_common_words


def get_sum_zero_pairs(numbers):
    """Given list of numbers, return list of pairs summing to 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.

    For example:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself):

        >>> sort_pairs( get_sum_zero_pairs([1, 3, -1, 1, 1, 0]) )
        [[-1, 1], [0, 0]]
    """
    # Initialize a list of pairs to store individual pairs that add up to 0
    unique_pairs = []

    # Generate a list of unique numbers to evaluate
    unique_numbers = list(set(numbers))

    # Iterate through each item in unique numbers to check if == 0
    for i, index in enumerate(unique_numbers):
        # Set the first integer to the currently-indexed element
        last_number = unique_numbers[i]

        # Iterate through each element in the list of unique numbers to evaluate
        for number in unique_numbers:
            # Calculate to see if the numbers add to 0
            if last_number + number == 0:
                # If the numbers add to 0 then create a list of the items and sort them 
                new_pair = sorted([last_number, number])
                # Make sure the list of numbers do not already exist in the list of unique_pairs to return
                if new_pair not in unique_pairs:
                    unique_pairs.append(new_pair)

    return unique_pairs


def top_chars(phrase):
    """Find most common character(s) in string.

    Given an input string, return a list of character(s) which
    appear(s) the most in the input string.

    If there is a tie, the order of the characters in the returned
    list should be alphabetical.

    For example:

        >>> top_chars("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example:

        >>> top_chars("Shake it off, shake it off.")
        ['f']

    Do not count spaces, but count all other characters.

    """

    # Get the given phrase without any white spaces
    alpha_phrase = phrase.split()

    # Initialize a dictionary to store each char as a key and occurrence of the char in the string as a count
    all_chars = {}

    # Iterate through the given phrase
    for word in alpha_phrase:
        # Iterate through the char of each word of the phrase
        for char in word:
            # Initialize the char key, value pair in the dictionary if not already exist
            if char not in all_chars:
                all_chars[char] = 1
            # Accumulate the value for the char key if already exist
            else:
                all_chars[char] += 1
    
    # Initialize an empty string to store the most common keys
    most_common_keys = ""
    current_count = 0

    for key in all_chars:
        if all_chars[key] > current_count:
            most_common_keys = key
            current_count = all_chars[key]
        elif all_chars[key] == current_count:
            most_common_keys += key

    # Get the most common keys as a list
    most_common_chars = list(most_common_keys)
    
    return most_common_chars


#####################################################################
# You can ignore everything below this.


def sort_pairs(l):
    """ Print sorted list of pairs where the pairs are sorted."""
    # NOTE: This is used only for documentation tests. You can ignore it.

    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print()
    import doctest
    if doctest.testmod().failed == 0:
        print("*** ALL TESTS PASSED ***")
    print()
