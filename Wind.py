from __future__ import annotations
from typing import List
from numpy import ndarray, array, float64, exp, log
from numpy.random import normal, uniform

β = 1 / (2 * log(2))

# wind speeds: ~[[1.3, 3.1] N/NE heading, [7.2, 11.2] N/NE] m/s +/- 10%

class Wind:
  avg_direction: ndarray
  uncert_direction: float
  avg_speed: float
  uncert_speed: float
  frequency: float
  uncert_frequency: float
  
  direction: ndarray
  speed: float
  t_offset: float = 0.0
  A: float
  decay_rate: float = 1.0
  
  def __init__(
    self,
    avg_direction: ndarray,
    uncert_direction: float,
    avg_speed: float,
    uncert_speed: float,
    frequency: float,
    uncert_frequency: float,
    decay_rate: float
  ):
    if len(avg_direction) != 3:
      raise ValueError("avg_direction argument in Wind class must be 3-dimensional!")
    
    self.avg_direction = avg_direction
    self.uncert_direction = uncert_direction
    self.avg_speed = avg_speed
    self.uncert_speed = uncert_speed
    self.frequency = frequency
    self.uncert_frequency = uncert_frequency
    
    self.A = avg_speed / decay_rate * exp(decay_rate * decay_rate)
    
    self.direction = self.getComponents()
    self.speed = self.getSpeed(t=0.0)
  
  def getComponents(self) -> ndarray:
    dx = normal(self.avg_direction[0], self.uncert_direction)
    dy = normal(self.avg_direction[1], self.uncert_direction)
    dz = 0.0
    
    norm = (dx * dx + dy * dy + dz * dz) ** 0.5
    
    dx /= norm
    dy /= norm
    dz /= norm
    
    return array([dx, dy, dz], dtype=float64)
  
  def getSpeed(self, t: float) -> float:
    return self.A * (t - self.t_offset) * exp(-self.decay_rate * (t - self.t_offset))
  
  def step(self, t: float) -> ndarray:
    if uniform(0, 1) < exp(-self.frequency * (t - self.t_offset) / β):
      self.t_offset = t
      self.direction = self.getComponents()
    
    return self.getWind(t=t)
  
  def getWind(self, t: float) -> ndarray:
    self.speed = self.getSpeed(t=t)
    return self.speed * self.direction