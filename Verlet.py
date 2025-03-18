from numpy import ndarray

def Verlet(f: function, r: ndarray, t: float, dt: float) -> ndarray:
  r_half = f(r, t)
  r_full = f(r + r_half * dt / 2, t + dt / 2)
  return dt * r_full