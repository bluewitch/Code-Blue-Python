if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    """
    pythonListComprehensions.py
    You are given three integers  and  representing the dimensions of a cuboid along with an           integer . You have to print a list of all possible coordinates given by  on a 3D grid where       the sum of is not equal to.
    """
    
    print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n ])
