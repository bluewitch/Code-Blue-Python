# Complete the solve function below.
def solve(string):
    stringList = string.split(" ")
    refinedList =[]
    for word in stringList:
        newWord = word[:1].upper() + word[1:]
        refinedList.append(newWord)
    newString = (" ").join(refinedList)
    return newString
