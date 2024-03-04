def dist_l1(u,v):
    """
    dist_l1([0,1,2], [1,2,3])
    >>> 3
    
    """
    result = 0
    
    for u1,v1 in zip(u, v):
        result += abs(u1-v1)
        
    return result

def dist_l2(u,v):
    """
    dist_l2([0,1,2], [1,2,3])
    >>> 3
    """
    
    result = 0
    
    for u1,v1 in zip(u, v):
        result += (u1-v1)**2
        
    return result

def dist_linf(u,v):
    """
    dist_linf([0,1,2], [1,2,3])
    >>> 1
    """
    highest = 0
        
    for u1,v1 in zip(u, v):

        dist = abs(u1-v1)
        highest = dist if dist > highest else highest
        
    return highest

def promedio(u):
    """
    promedio([0,1,2])
    >>> 1
    """
    return sum(u)/len(u)

def desv_est(u):
    """
    desv_est([0,1,2])
    >>> 0.444
    """
    prom = promedio(u)
    num = sum([(u1-prom)**2 for u1 in u])
    result = (num/len(u))**0.5
    
    return result

def varianza(u):
    """
    varianza([0,1,2])
    >>> 0.666
    """
    return desv_est(u)**2



