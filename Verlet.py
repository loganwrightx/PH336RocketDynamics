from numpy import ndarray

def velocity_verlet(x, v, dt, accel):
    a = accel(x)
    x_new = x + v*dt + 0.5*a*dt*dt
    a_new = accel(x_new)
    v_new = v + 0.5*(a + a_new)*dt
    return x_new, v_new

def Verlet(f: function, r: ndarray, t: float, dt: float) -> ndarray:
  r_half = f(r, t)
  r_full = f(r + r_half * dt / 2, t + dt / 2)
  return dt * r_full