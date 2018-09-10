if __name__ == '__main__':
    s = input()
    #List Comprehensions
    print(bool(len([ch for ch in s if ch.isalnum()])))
    print(bool(len([ch for ch in s if ch.isalpha()])))
    print(bool(len([ch for ch in s if ch.isdigit()])))
    print(bool(len([ch for ch in s if ch.islower()])))
    print(bool(len([ch for ch in s if ch.isupper()])))
