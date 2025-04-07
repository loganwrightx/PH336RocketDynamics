from numpy import array, float64, std, mean
from Differentials import reset_wind
from LaunchLoop import loop

if __name__ == "__main__":
  ts = []
  zs = []
  rs = []
  N = 1
  
  for _ in range(N):
    reset_wind()
    
    t, z_max, radial_dist = loop(
      θ=0.0,
      φ=0.0,
      v0=0,
      dt=1e-3,
      r0=array([0.0, 0.0, 0.0], dtype=float64),
      plot=True
    )
    
    #print(f"Completed loop #{_ + 1}")
    
    ts.append(t)
    zs.append(z_max)
    rs.append(radial_dist)
  
  print(f"Time of flight: {mean(ts):.3f} +/- {std(ts):.3f} s")
  print(f"Maximum altitude: {mean(zs):.3f} +/- {std(zs):.3f} m")
  print(f"Radial distance away from launch zone: {mean(rs):.3f} +/- {std(rs):.3f} m")