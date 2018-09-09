def is_leap(year):
    leap = False
    
    # Write your logic here
    # thought process
    #if year%4==0:
    #    return True
    #elif year%100==0:
    #    return False
    #elif year%400==0:
    #    return True
    
    # Optimized, Python 3
    return ((year%4==0)and(year%100!=0)or(year%400==0))
