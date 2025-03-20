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

    while r[R, Z] >= 0.0:
        dr = RK4(f, r, t, dt)
        
        if t < 0.2 and dr[R_DOT, Z] < 0.0:
            dr[R, Z] = 0
            dr[R_DOT, Z] = 0 # Keep the rocket from going down when gravity is initially greater than thust

        r += dr
        t += dt # dt defined in main
        
        x_list.append(r[R, X])
        y_list.append(r[R, Y])
        z_list.append(r[R, Z])
        vx_list.append(r[R_DOT, X])
        vy_list.append(r[R_DOT, Y])
        vz_list.append(r[R_DOT, Z])
        t_list.append(t)
    
    max_height = max(z_list)
    
    if plot:
        fig, axs = plt.subplots(2, 3)
        axs: Union[Axes, ndarray[Axes]]
        axs.reshape(2, 3)
        fig.tight_layout()
        axs[0, 0].plot(t_list, x_list)
        axs[0, 1].plot(t_list, y_list)
        axs[0, 2].plot(t_list, z_list)
        axs[1, 0].plot(t_list, vx_list)
        axs[1, 1].plot(t_list, vy_list)
        axs[1, 2].plot(t_list, vz_list)
        plt.show()

    return t, max_height


