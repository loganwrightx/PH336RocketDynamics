from numpy import array, ndarray, sin, cos, copy, float64
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from typing import Union

from Differentials import f
from RK4 import RK4

plt.style.use("dark_background")

R, R_DOT, X, Y, Z = 0, 1, 0, 1, 2

def loop(θ: float, φ: float, v0: float, dt: float, r0: ndarray, plot: bool = False):
    t = 0
    v0 = array([v0 * cos(φ) * sin(θ), v0 * sin(φ) * sin(θ), v0 * cos(θ)], dtype=float64)
    r0 = copy(r0)
    
    if len(r0) != 3:
        raise ValueError("r0 vector must have exactly 3 values initially!")
    
    r = array([r0, v0], dtype=float64)
    
    t_list = [t]
    x_list = [r[R, X]]
    y_list = [r[R, Y]]
    z_list = [r[R, Z]]
    vx_list = [r[R_DOT, X]]
    vy_list = [r[R_DOT, Y]]
    vz_list = [r[R_DOT, Z]]

    while r[R, Z] >= -1e-3:
        dr = RK4(f, r, t, dt)
        
        if t < 0.5 and dr[R_DOT, Z] < 0.0:
            dr[R, Z] = 0
            dr[R_DOT, Z] = 0
        
        r += dr
        t += dt
        
        x_list.append(r[R, X])
        y_list.append(r[R, Y])
        z_list.append(r[R, Z])
        vx_list.append(r[R_DOT, X])
        vy_list.append(r[R_DOT, Y])
        vz_list.append(r[R_DOT, Z])
        t_list.append(t)
    
    if plot:
        fig, axs = plt.subplots(2, 3)
        axs: Union[Axes, ndarray[Axes]]
        axs.reshape(2, 3)
        
        axs[0, 0].plot(t_list, x_list)
        axs[0, 0].set_title("x vs t")
        
        axs[0, 1].plot(t_list, y_list)
        axs[0, 1].set_title("y vs t")
        
        axs[0, 2].plot(t_list, z_list)
        axs[0, 2].set_title("z vs t")
        
        axs[1, 0].plot(t_list, vx_list)
        axs[1, 0].set_title("vx vs t")
        
        axs[1, 1].plot(t_list, vy_list)
        axs[1, 1].set_title("vy vs t")
        
        axs[1, 2].plot(t_list, vz_list)
        axs[1, 2].set_title("vz vs t")
        
        fig.tight_layout()
        
        plt.show()

    return t_list[-1], max(z_list), (x_list[-1] * x_list[-1] + y_list[-1] * y_list[-1]) ** 0.5


