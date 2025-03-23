from __future__ import annotations
from typing import List
from numpy import ndarray, array, float64, exp
from numpy.random import normal as random_normal

class Wind:
  wind_direction: ndarray
  direction_var: float
  ambient_speed: float
  gust_speed: float
  speed_var: float
  gust_frequency: float
  frequency_var: float
  
  def __init__(self,
    wind_direction: ndarray,
    direction_var: float,
    ambient_speed: float,
    gust_speed: float,
    speed_var: float,
    gust_frequency: float,
    frequency_var: float
  ):
    self.wind_direction = wind_direction
    self.direction_var = direction_var
    self.ambient_speed = ambient_speed
    self.gust_speed = gust_speed
    self.speed_var = speed_var
    self.gust_frequency = gust_frequency
    self.frequency_var = frequency_var
    

class Gust:
  def __init__(self, t0: float):
    self.t0 = t0
  
  def __getitem__(self, i: int) -> tuple[float, bool]:
    return 