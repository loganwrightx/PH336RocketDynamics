from Differentials import f
from RK4 import RK4
from numpy import array, ndarray, sin, cos
import matplotlib.pyplot as plt

plt.style.use("dark_background")

R, R_DOT, X, Y = 0, 1, 0, 1

def loop(θ: float, v: float, dt: float, r0: ndarray, plot: bool = False):
    t = 0
    v0 = array([v0 * sin(θ), v0 * cos(θ)], dtype=float)
    r = array([r0, v0], dtype=float)
    
    t_list = [t]
    x_list = [r[R, X]]
    y_list = [r[R, Y]]

    while r[R, Y] >= 0:
        dr = RK4(f, t, dt)
        
        if t < 0.1 and dr[R_DOT, Y] < 0:
            dr[R_DOT, Y] = 0 # Keep the rocket from going down when gravity is initially greater than thust

        r += dr
        t += dt # dt defined in main
        
        x_list.append(r[R, X])
        y_list.append(r[R, Y])
        t_list.append(t)
    
    max_height = max(y_list)
    
    if plot:
        plt.plot(t_list, x_list)
        plt.plot(t_list, y_list)
        plt.show()

    return t, max_height


