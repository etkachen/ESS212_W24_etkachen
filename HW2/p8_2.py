import numpy as np
import matplotlib.pyplot as plt

# dt is the time step
# h is height from the ground
# The function will print out Wille-E's height at each time step

def p8_2(dt, h):
    z = np.zeros(1000)
    v = np.zeros(1000)
    z[0] = 0
    ts = 0
    i = 0
    v[0] = 0
    while (z[i] > -h):
        print("At t =", ts, "s, Wille-E's height =", z[i], "m.")
        i = i+1
        ts = ts + dt
        v[i] = v[i-1] - 9.81*dt
        z[i] = z[i-1] + v[i-1]*dt
    print("SLAM to the ground at t =", ts, "s.")
    return z[:i+1],v[:i+1]
    
    
z,v = p8_2(1, 1000)
plt.plot(0.5*11.5*(v**2), label = "Kinetic energy, J")
plt.plot(11.5*9.81*z, label = "Potential energy, J")
plt.plot(0.5*11.5*(v**2) + 11.5*9.81*z, label = "Total energy, J")
plt.xlabel("Time, s")
plt.title("Energy balance, Problem 8b")
plt.legend()
plt.show()