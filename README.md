# Experiment Description

This project is an RK4 solver for a rocket subject to aerodynamic loads and nonlinear forces. The models simulated in this environment are to support real experiments over the course of several weeks.

The goal of the experiments are to prove/improve our model of a rocket in an aerodynamic environment with statistical methods, Monte Carlo algorithms, and numerical integrators. Data is to be collected from the vehicle in flight and the characteristics of its performance will be compared to the results of the simulations. Iterative methods will be used to estimate an average behavior of the system and approximate uncertainties of those behaviors. Since RK4 is fast, computational simulation time can be very efficiently used to estimate system performance according to the model, and data collected will have a greater impact on validating/disproving our model.

# The Physical Model

The analysis of a rocket trajectory requires a precise description of the forces acting on the body. The exhaustive list for the purpose of this project is shown below:

- Air resistance, acts opposite to te direction of velocity and is proportional to the square of the vehicle speed

- Gravity, always points toward earth's center which is the local negative y coordinate

- Thrust force, point in the same direction as velocity but it's magnitude is time and motor dependent

- When thrust is non-zero, mass is reduced in time from the vehicle also contributing to a change in momentum

- And finally, aerodynamic forces on the body from the sides induced by wind are also accounted for, and operate under normally distributed random processes

Using Newton's second law, it follows that

$$ \sum \vec{F} = \vec{T(t)} - \vec{F}_ {\text{Drag}} - \vec{F}_ {g} - \vec{F}_{\text{Aero}} = m(t) \cdot \ddot{\vec{r}} $$

This is the differential equation that the simulator aims to solve.

# Motor Model

The rocket uses an Estes A8 solid propellant rocket motor. Thrust curve data is publicly available and free for use. Our team did not collect the data, but we use to it model the performance of the motors in our experiments. We use linear interpolation to create a continuous representation of the thrust curve and incorporate small deviations from the data with Monte Carlo methods according to the uncertainties in the motor design. For our purposes, simulations use $\delta{T} = \pm 1$% up to $\delta{T} = \pm 5$%. 

If time permits, and if we need to optimize our computational model, we can generate our own thrust curve data by positioning the engine in a wood block on top of a force sensor. We can measure the force as a function of time and take the average of several acquisitions. 

# Atmospheric Model

We use the NASA tropospheric model. Since we are operating at low altitudes, this will be sufficiently accurate for the case of modeling air density, and thus drag forces.

# Wind Model

Our wind model consists of a simple normally distributed wind gust model and a small continuous form breeze in a constant direction. Monte Carlo will also be used for computing a random initial direction for the wind.

# Uncertainty Propagation

Uncertainty will be computed using iterative methods. Since RK4 is so fast and flight times will likely last less than 10 seconds in real time, computation time is extremely small per iteration. To approximate our expected performance parameters (max altitude, flight time, landing zone, etc), the simulation will be run hundreds of times and averages over them all with standard deviations representing the associated uncertainties.

# Materials List

- Model rocket

- Estes A8 motors, ~10 of them

- Computer with Python 3.13 installed

- Timer

- Accelerometer sensor, barometric pressure sensor, Arduino Nano, and SD card logger

- Soldering iron

- Launch supplies (launch pad, igniter for motors)

- Lab notebooks and pens

- Wood block and force sensor

- Protractor

- GPS for measuring horizontal travel distance (phones might suffice)

# Expected Results

We expect our experimental results for flight time, maximum altitude, and horizontal distance traveled to pass a Chi-Squared Test ($\alpha = .05$) when compared with our Monte-Carlo simulation. Further refinement with our wind model may be necessary if time permits.

# Timeline

We expect to have completed our computational model by the 20th of Thursday, after which we will collect our computational data. We will then, if time permits, acquire thrust curve data using a force sensor. During the following week, we will monitor weather and select an optimal launch day. We expect the setup, launch, and data acquisition to take no more than three hours. The next week will be dedicated to data analysis, model refinement, and re-acquiring data if necessary.
