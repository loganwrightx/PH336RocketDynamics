from numpy import ndarray
# verlet seems pretty cool, I don't remember learning about it
# Is this somewhat the idea?

def velocity_verlet(x, v, dt, accel):
    a = accel(x)
    x_new = x + v*dt + 0.5*a*dt*dt
    a_new = accel(x_new)
    v_new = v + 0.5*(a + a_new)*dt
    return x_new, v_new

def Verlet(f: function, r: ndarray, t: float, dt: float, response: float = None) -> ndarray:
  r_half = f(r, t, response)
  r_full = f(r + r_half * dt / 2, t + dt / 2, response)
  return dt * r_full