#Copy pasted from 295
def RK4(f, r, t, h):
    k1 = h*f(r,t)
    k2 = h*f(r+.5*k1, t+.5*h)
    k3 = h*f(r+.5*k2, t+.5*h)
    k4 = h*f(r+k3, t+h)
    return (k1+ 2*k2 + 2*k3 +k4)/6
