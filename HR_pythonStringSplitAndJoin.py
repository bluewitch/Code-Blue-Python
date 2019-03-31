def split_and_join(line):
    """
    Split and join is a simple function that illustrates some string manipulation by creating a variable named line, 
    using the embedded .split() method, to convert to a list of strings and interposing a - character by way of 
    the .join method, and returning the value of the line variable.
    """
    # write your code here
    line = line.split(" ") # a is converted to a list of strings.
    line = "-".join(line)
    return(line)
