def count_substring(string, sub_string):
    """
    This is a simple function that returns a List Comprehension to find the substrings within character strings, 
    outputing the total number of occurrences of the substring in the original string
    """
    # List Comprehension
    return(sum([1 for i in range(0, len(string) - len(sub_string) + 1) if (string[i:(len(sub_string)+i)] == sub_string)]))
