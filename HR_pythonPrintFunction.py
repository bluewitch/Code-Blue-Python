import sys

if __name__ == '__main__':
    n = int(input())
 
    # imported sys for a elegant solution, Python 3
    # * before range means taking everything 0 or more
    print(*range(1,n+1), sep='',end='\n', file= sys.stdout)
