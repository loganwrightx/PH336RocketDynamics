from numpy import array, tan, cos, mean, std, pi, sqrt

### Day 1 ###

print("Day One")

Δt_vals = array([7.97,8.52,6.72,6.75,6.75,6.52]) 
Δx_vals = array([2.36,6.43,14.50,12.2,9.0])

d1_val, δd1 = 30, 1
θ1_vals = array([59,56,62,55,63,54]) * pi/180

d2_val, δd2 = 50, 1
θ2_vals = array([39,48,30,50,42,40]) * pi/180

θ1, δθ1 = mean(θ1_vals), std(θ1_vals)
θ2, δθ2 = mean(θ2_vals), std(θ2_vals)

y1 = d1_val * tan(θ1)
δy1 = ((δθ1 * d1_val / ((cos(θ1))**2))**2 + (tan(θ1)*δd1)**2)**.5

y2 = d2_val * tan(θ2)
δy2 = ((δθ2 * d2_val / ((cos(θ2))**2))**2 + (tan(θ1)*δd2)**2)**.5

y_total = ((y1/δy1**2) + (y2/δy2**2)) / ((1/δy1**2) + (1/δy2**2))
δy_total = 1 / ((1/δy1**2) + (1/δy2**2))**.5

hang_time, δhang_time = mean(Δt_vals), std(Δt_vals)
horizontal_distance, δhorizontal_distance = mean(Δx_vals), std(Δx_vals)

print(f"Measured Time of Flight: {hang_time:.2f} +/- {δhang_time:.2f} s")
print(f"Measured Height: {y_total:.2f} +/- {δy_total:.2f} m")
print(f"Measured Radial Distance: {horizontal_distance:.2f} +/- {δhorizontal_distance:.2f} m")


###### Chi Squared #######

from scipy import stats

MC_TOF, δMC_TOF = 7.204, .01
MC_alt, δMC_alt = 57.109, .160
MC_dist, δMC_dist = 6.072, .015

print(f"\nSimulated Time of Flight: {MC_TOF:.2f} +/- {δMC_TOF:.2f} s")
print(f"Simulated Height: {MC_alt:.2f} +/- {δMC_alt:.2f} m")
print(f"Simulated Radial Distance: {MC_dist:.2f} +/- {δMC_dist:.2f} m\n")

expected_dist = array([MC_TOF,MC_alt,MC_dist])
measured_dist = array([hang_time, y_total, horizontal_distance])

σs = array([sqrt(δMC_TOF**2 + δhang_time**2),sqrt(δMC_alt**2 + δy_total**2),sqrt(δMC_dist**2 + δhorizontal_distance**2)])

χ2 = sum(((measured_dist-expected_dist)**2) / (σs**2))
dof = (3-1)*(2-1)

P = 1 - stats.chi2.cdf(χ2, dof)

print(f"P-Value: {P:.4f}\n")

### Day 2 ###

print("Day Two")

Δt_vals = array([7.4,7.7,7.35,7.02]) 
Δx_vals = array([17, 6, 21, 43])

d1_val, δd1 = 40, 1
θ1_vals = array([37,44,48,32]) * pi/180

d2_val, δd2 = 40, 1
θ2_vals = array([41,44,55,45]) * pi/180

θ1, δθ1 = mean(θ1_vals), std(θ1_vals)
θ2, δθ2 = mean(θ2_vals), std(θ2_vals)

y1 = d1_val * tan(θ1)
δy1 = ((δθ1 * d1_val / ((cos(θ1))**2))**2 + (tan(θ1)*δd1)**2)**.5

y2 = d2_val * tan(θ2)
δy2 = ((δθ2 * d2_val / ((cos(θ2))**2))**2 + (tan(θ1)*δd2)**2)**.5

y_total = ((y1/δy1**2) + (y2/δy2**2)) / ((1/δy1**2) + (1/δy2**2))
δy_total = 1 / ((1/δy1**2) + (1/δy2**2))**.5

hang_time, δhang_time = mean(Δt_vals), std(Δt_vals)
horizontal_distance, δhorizontal_distance = mean(Δx_vals), std(Δx_vals)

print(f"Measured Time of Flight: {hang_time:.2f} +/- {δhang_time:.2f} s")
print(f"Measured Height: {y_total:.2f} +/- {δy_total:.2f} m")
print(f"Measured Radial Distance: {horizontal_distance:.2f} +/- {δhorizontal_distance:.2f} m")


###### Chi Squared #######

from scipy import stats

MC_TOF, δMC_TOF = 7.143, .009
MC_alt, δMC_alt = 56.093, .142
MC_dist, δMC_dist = 33.585, .071

print(f"\nSimulated Time of Flight: {MC_TOF:.2f} +/- {δMC_TOF:.2f} s")
print(f"Simulated Height: {MC_alt:.2f} +/- {δMC_alt:.2f} m")
print(f"Simulated Radial Distance: {MC_dist:.2f} +/- {δMC_dist:.2f} m\n")

expected_dist = array([MC_TOF,MC_alt,MC_dist])
measured_dist = array([hang_time, y_total, horizontal_distance])

σs = array([sqrt(δMC_TOF**2 + δhang_time**2),sqrt(δMC_alt**2 + δy_total**2),sqrt(δMC_dist**2 + δhorizontal_distance**2)])

χ2 = sum(((measured_dist-expected_dist)**2) / (σs**2))
dof = (3-1)*(2-1)

P = 1 - stats.chi2.cdf(χ2, dof)

print(f"P-Value: {P:.4f}")