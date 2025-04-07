from __future__ import annotations
from numpy import linspace
from matplotlib.pyplot import plot, xlabel, show, style, legend

C_TO_K = 273.15

class Troposphere:
  def __init__(self, ambient_temp: float):
    self.ambient_temp = ambient_temp
    
  def t(self, altitude: float) -> float:
    return self.ambient_temp - 0.00649 * altitude
  
  def p(self, altitude: float) -> float:
    _t = self.t(altitude)
    return 101.29 * ((_t + C_TO_K) / 288.08) ** 5.256
  
  def rho(self, altitude: float) -> float:
    _p = self.p(altitude)
    _t = self.t(altitude)
    return _p / (0.2869 * (_t + C_TO_K))

if __name__ == "__main__":
  t = Troposphere(ambient_temp=10.0)
  
  zs = linspace(0.0, 1000.0, num=1000)
  rhos = [t.rho(z) for z in zs]
  ts = [t.t(z) for z in zs]
  ps = [t.p(z) for z in zs]
  
  style.use("classic")
  xlabel("altitude (m)")
  plot(zs, rhos)
  plot(zs, ts)
  plot(zs, ps)
  legend(["ρ(z)", "T(z)", "p(z)"])
  show()