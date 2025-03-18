# verlet seems pretty cool, I don't remember learning about it
# Is this somewhat the idea?

def velocity_verlet(x, v, dt, accel):
    a = accel(x)
    x_new = x + v*dt + 0.5*a*dt*dt
    a_new = accel(x_new)
    v_new = v + 0.5*(a + a_new)*dt
    return x_new, v_new
