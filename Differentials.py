from numpy import ndarray, array, pi, dot, float64
from numpy.linalg import norm
from Thrust import T, T_experimental_data, get_data, get_linear_interpolations
from Troposphere import Troposphere
from Wind import Wind

temp = 0.0 # celsius ambient temperature outside || data: [7.2, 16.7] degrees C
Cd = 0.5
A = 0.013 ** 2 * pi
m = 0.100
g = 9.81

side_area = 0.026 * 0.66

troposphere = Troposphere(temp)
wind = Wind(avg_direction=array([1.0, 0.0, 0.0]), uncert_direction=0.5, avg_speed=1.3, uncert_speed=0.5, frequency=0.1, uncert_frequency=0.01, decay_rate=5)

thrust_data = get_data()
interpolations = get_linear_interpolations(thrust_data)

R, V, X, Y, Z = 0, 1, 0, 1, 2

def f(r: ndarray, t: float) -> ndarray:
  """
  r: [[x, y, z], [vx, vy, vz]]
  
  F = ma = - F_drag - F_gravity + Thrust [+ Wind] <- will incorporate this later
  """
  rho = troposphere.rho(r[R, Z])
  v_wind = wind.step(t=t)
  v = r[V]
  
  if abs(norm(v)) > 0.0:
    a = (-1 / 2 * rho * Cd * A * dot(v, v) * v / norm(v) - \
      m * array([0.0, 0.0, g], dtype=float64) + T_experimental_data(t) * array([0.0, 0.0, 1.0], dtype=float64)) / m
  else:
    a = (-m * array([0.0, 0.0, g], dtype=float64) + T_experimental_data(t) * array([0.0, 0.0, 1.0], dtype=float64)) / m
  
  if (n := norm(v_wind - v)) > 0.0:
    a += 1 / 2 * rho * Cd * side_area * dot((v_wind - v), (v_wind - v)) * (v_wind - v) / n / m
  
  return array([v, a], dtype=float64)