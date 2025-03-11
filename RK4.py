#Copy pasted from 295, I know it will need modification
def rk4(f, r, t, tf, h, thetalist, tlist):
    while t<tf:
        k1 = h*f(r,t)
        k2 = h*f(r+.5*k1, t+.5*h)
        k3 = h*f(r+.5*k2, t+.5*h)
        k4 = h*f(r+k3, t+h)

        #estimate new r
        r += (k1+ 2*k2 + 2*k3 +k4)/6

        # add new values to the lists for plotting
        thetalist.append(r[0])
        t += h
        tlist.append(t)