from __future__ import annotations
from numpy.random import normal as random_normal
from numpy import ndarray, zeros, exp
from scipy.stats import norm


class Wind:
  decay_rate = 0.5
  def __init__(self, wind_speed: float = 0.1, probability_of_gust: float = 0.05):
    self.z_score = norm.ppf(1 - probability_of_gust / 2)
    self.wind_speed: float = wind_speed
  
  def _p(self, altitude: float) -> float:
    return self.z_score * exp(-altitude / 10)
  
  def step(self, altitude: float) -> ndarray:
    _wind = zeros(shape=(1, 3), dtype=float)
    if abs(r:=random_normal()) > 1.96:
      _wind[0] = r

if __name__ == "__main__":
  w = Wind()
  print(norm.ppf(0.95 + 0.025))