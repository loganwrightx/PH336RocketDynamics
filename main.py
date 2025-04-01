from numpy import array, float64, std, mean
from LaunchLoop import loop

if __name__ == "__main__":
  ts = []
  zs = []
  N = 5
  
  for _ in range(N):
    t, z_max = loop(
      θ=0.0,
      φ=0.0,
      v0=0,
      dt=1e-3,
      r0=array([0.0, 0.0, 0.0], dtype=float64),
      plot=True
    )
    
    ts.append(t)
    zs.append(z_max)
  
  print(zs)
  print(f"Time of flight: {mean(ts):.3f} +/- {std(ts):.3f} s")
  print(f"Maximum altitude: {mean(zs):.3f} +/- {std(zs):.3f} m")