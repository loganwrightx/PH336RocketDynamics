

from Differentials import f
from RK4 import rk4
from numpy import array, transpose


def loop(θ, dt, x0, y0, vx0, vy0):
    t = 0
    
    #
    t_list = [0]
    r_list = [[x0, y0]]
    

    while y >= 0:
        if t < 0.1 and ay < 0:
            ay = 0 #Keep the rocket from going down when gravity is initially greater than thust

        dr = rk4(f, t, dt)
        r_list.append([r[0,0], r[0,1]])

        r += dr 
        t += dt #dt defined in rk4
        
        #Transposes r_list so that it's easy to find the maximum y value
        max_height = max(transpose(array(r_list))[1])

    return t, max_height


