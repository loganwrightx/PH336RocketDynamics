from __future__ import annotations
from typing import NamedTuple, List, TypeAlias, overload
from pandas import read_csv, DataFrame
from numpy import ndarray, array, linspace, zeros
from numpy.random import normal as random_normal
import matplotlib.pyplot as plt
from experimental_thurstcurve import cs, total_time, avg_stdev

data_dir = "./ThrustData.csv"

δT = avg_stdev

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

@overload
def T(t: float) -> float: ...

@overload
def T(t: ndarray) -> ndarray: ...

def T(t: float | ndarray, interpolations: Interpolations):
  """ gets linearly interpolated A8 thrust curve value at t = t

  Args:
      t (float): current time
      interpolations (List[Interpolation]): interpolation list data

  Returns:
      float: thrust force magnitude
  """
  if isinstance(t, ndarray):
    out = zeros(shape=t.shape, dtype=float)
    for idx, _t in enumerate(t):
      for interpolation in interpolations:
        if _t >= interpolation.start_time and _t < interpolation.stop_time:
          out[idx] ((_t - interpolation.start_time) * interpolation.slope + interpolation.y_intercept) * (1 + random_normal() * δT)
    
    return out
  
  elif isinstance(t, float):
    for interpolation in interpolations:
      if t >= interpolation.start_time and t < interpolation.stop_time:
        return ((t - interpolation.start_time) * interpolation.slope + interpolation.y_intercept) * (1 + random_normal() * δT)
  
  return 0.0

def T_experimental_data(t: float) -> float:
  if 0.0 <= t <= (total_time[-1] - total_time[0]):
    return cs(t + total_time[0]) + δT * random_normal()
  else:
    return 0.0

class Interpolation(NamedTuple):
  start_time: float
  stop_time: float
  y_intercept: float
  slope: float

Interpolations: TypeAlias = List[Interpolation]

if __name__ == "__main__":
  t = linspace(0.0, total_time[-1] - total_time[0], 100)
  
  plt.plot(t, [T_experimental_data(_t) for _t in t])
  plt.show()