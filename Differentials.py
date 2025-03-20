from numpy import ndarray, array, pi, dot, float64
from numpy.linalg import norm
from Thrust import T, T_experimental_data, get_data, get_linear_interpolations
from Troposphere import Troposphere

temp = 0.0 # celsius ambient temperature outside
Cd = 0.5
A = 0.0015 ** 2 * pi
m = 0.100
g = 9.81

troposphere = Troposphere(temp)

thrust_data = get_data()
interpolations = get_linear_interpolations(thrust_data)

R, V, X, Y, Z = 0, 1, 0, 1, 2

def f(r: ndarray, t: float) -> ndarray:
  """
  r: [[x, y, z], [vx, vy, vz]]
  
  F = ma = - F_drag - F_gravity + Thrust [+ Wind] <- will incorporate this later
  """
  rho = troposphere.rho(r[R, Z])
  v = r[V]
  if abs(norm(v)) > 0.0:
    a = (-1 / 2 * rho * Cd * A * dot(v, v) * v / norm(v) - \
      m * array([0.0, 0.0, g], dtype=float64) + T_experimental_data(t, interpolations) * array([0.0, 0.0, 1.0], dtype=float64)) / m
  else:
    a = (-m * array([0.0, 0.0, g], dtype=float64) + T_experimental_data(t, interpolations) * array([0.0, 0.0, 1.0], dtype=float64)) / m
  
  return array([v, a], dtype=float64)