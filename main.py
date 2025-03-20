from numpy import array, float64
from LaunchLoop import loop

if __name__ == "__main__":
  t, z_max = loop(
    θ=0.0,
    φ=0.0,
    v0=0,
    dt=1e-3,
    r0=array([0.0, 0.0, 0.0], dtype=float64),
    plot=True
  )
  
  print(z_max, t)