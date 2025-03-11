from __future__ import annotations
from typing import NamedTuple, List, TypeAlias
from pandas import read_csv, DataFrame
from numpy import ndarray, array, linspace
from numpy.random import normal as random_normal
import matplotlib.pyplot as plt

data_dir = "./ThrustData.csv"

δT = 0.01

def get_data(data_dir = data_dir) -> DataFrame:
  return read_csv(data_dir)

def get_linear_interpolations(data: DataFrame) -> Interpolations:
  _interpolations = []
  _t = data["t"].to_numpy()
  _T = data["T"].to_numpy()
  for i in range(len(_t) - 1):
    _start_time = _t[i]
    _stop_time = _t[i + 1]
    _y_intercept = _T[i]
    _slope = (_T[i + 1] - _T[i]) / (_t[i + 1] - _t[i])
    _interpolations.append(Interpolation(start_time=_start_time, stop_time=_stop_time, y_intercept=_y_intercept, slope=_slope))
  
  return _interpolations

def T(t: float, interpolations: Interpolations) -> float:
  """ gets linearly interpolated A8 thrust curve value at t = t

  Args:
      t (float): current time
      interpolations (List[Interpolation]): interpolation list data

  Returns:
      float: thrust force magnitude
  """
  for interpolation in interpolations:
    if t >= interpolation.start_time and t < interpolation.stop_time:
      return ((t - interpolation.start_time) * interpolation.slope + interpolation.y_intercept) * (1 + random_normal() * δT)
  
  return 0.0

class Interpolation(NamedTuple):
  start_time: float
  stop_time: float
  y_intercept: float
  slope: float

Interpolations: TypeAlias = List[Interpolation]

if __name__ == "__main__":
  df = get_data()
  inter = get_linear_interpolations(df)
  t = linspace(0.0, 0.6, num=100)
  T_data = array([T(_t, inter) for _t in t])
  
  plt.plot(t, T_data)
  plt.show()