def three_n_plus_1(num):
    """
    three_n_plus_1(4)
    >>> 2
    
    three_n_plus_1(6)
    >>> 8
    
    three_n_plus_1(1)
    >>> 0
    """
    
    steps = 0
    
    while True:
        if num % 2 == 0:
            num /= 2
            
        elif num == 1:
            break
        
        else:
            num = 3*num+1
            
        steps += 1
        
    return steps