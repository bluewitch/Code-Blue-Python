if __name__ == '__main__':
    n = int(input())

    #FROM THIS
    #counter = 0;
    #while  counter < n :
    #    print (counter**2)
    #    counter = counter + 1
    
    #TO THIS
    #List comprehension, Python 3
    [print(i**2) for i in range(n)]
