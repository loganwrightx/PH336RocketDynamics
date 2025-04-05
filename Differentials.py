from numpy import ndarray, array, pi, dot, float64
from numpy.linalg import norm
from Thrust import T, T_experimental_data, get_data, get_linear_interpolations
from Troposphere import Troposphere
from Wind import Wind

temp = 0.0 # celsius ambient temperature outside || data: [7.2, 16.7] degrees C
Cd = 0.5
A = 0.013 ** 2 * pi
m0 = 0.0171 + 0.0481 # dm = 10.1g
m_dot = 0.0041 / 0.7 # change in mass, burn time is ~ 0.7 seconds
g = 9.81

m = lambda t: m0 - m_dot * t if t < 0.7 else m0 - m_dot * 0.7

side_area = 0.026 * 0.66

troposphere = Troposphere(temp)
wind = Wind(avg_direction=array([1.0, 0.0, 0.0]), uncert_direction=0.1, avg_speed=1.3, uncert_speed=0.13, frequency=0.2, uncert_frequency=0.05, decay_rate=1)

thrust_data = get_data()
interpolations = get_linear_interpolations(thrust_data)

R, V, X, Y, Z = 0, 1, 0, 1, 2

def reset_wind() -> None:
  global wind
  wind = Wind(avg_direction=array([1.0, 0.0, 0.0]), uncert_direction=0.1, avg_speed=1.3, uncert_speed=0.13, frequency=0.2, uncert_frequency=0.05, decay_rate=1)

def f(r: ndarray, t: float) -> ndarray:
  """
  r: [[x, y, z], [vx, vy, vz]]
  """
  rho = troposphere.rho(r[R, Z])
  v_wind = wind.step(t=t)
  v = r[V]
  
  a = array([0.0, 0.0, 0.0], dtype=float64)
  
  if (n := norm(v - v_wind)) > 0.0:
    a[2] = (-1 / 2 * rho * Cd * A * dot((v - v_wind), (v - v_wind)) * (v - v_wind)[2] / n - \
      m(t) * array([g], dtype=float64) + T_experimental_data(t) * array([1.0], dtype=float64)) / m(t)
    
    a[:2] -= 1 / 2 * rho * Cd * side_area * dot((v - v_wind), (v - v_wind)) * (v - v_wind)[:2] / n / m(t)
    
  else:
    a[2] = (-m(t) * array([g], dtype=float64) + T_experimental_data(t) * array([1.0], dtype=float64)) / m(t)
  
  return array([v, a], dtype=float64)