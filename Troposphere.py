from __future__ import annotations

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