import math
def cin_inv(x3,y3,z3,a1,a2,a3):
    
    
    r1 = (x3**2+y3**2)**0.5
    r2 = z3-a1
    r3 = (r1**2+r2**2)**0.5
    
    theta1 = math.atan2(y3,x3)
    theta2 = math.atan2(r2,r1) - math.acos((a3**2-a2**2-r3**2)/(-2*a2*r3))
    theta3 = 180 - math.acos(((r3**2)-(a2**2)-(a3**2))/(-2*a2*a3))
    
    return theta1, theta2, theta3