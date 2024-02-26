import numpy as np
import matplotlib.pyplot as plt

def p8_3(dt, h):
    z = np.zeros(1000)
    v = np.zeros(1000)
    z[0] = h
    ts = 0 
    i = 0 # iterator
    v[0] = 0
    while (z[i] > 0):
        if i % 2 == 0:
            print("At t =", ts, "s, Wille-E's height =", z[i], "m.")
        i = i + 1
        ts = ts + dt
        if i == 1:
            v[i] = 0 - 2*9.81*dt
            z[i] = h
        else:
            v[i] = v[i-2] - 2*9.81*dt
            z[i] = z[i-2] + 2*dt*v[i-1]
    print("SLAM to the ground at t =", ts, "s.")
    return z[:i+1],v[:i+1]
    
    
z, v = p8_3(1, 100)
print("Total energy average:", np.average(0.5*11.5*(v**2) + 11.5*9.81*z))
plt.plot(0.5*11.5*(v**2), label = "Kinetic energy, J")
plt.plot(11.5*9.81*z, label = "Potential energy, J")
plt.plot(0.5*11.5*(v**2) + 11.5*9.81*z, label = "Total energy, J")
plt.xlabel("Time, s")
plt.title("Energy balance, Problem 8c")
plt.legend()
plt.show()