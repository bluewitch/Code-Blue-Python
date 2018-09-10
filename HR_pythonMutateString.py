# pythonMutateString.py
def mutate_string(string, position, character):
    # Yet another, Python one liner...
    return string[:position] + character + string[position + 1:]
