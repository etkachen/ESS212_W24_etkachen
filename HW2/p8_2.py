import numpy as np
import matplotlib.pyplot as plt

# dt is the time step
# h is height from the ground
# The function will print out Wille-E's height at each time step

def p8_2(dt, h):
    # Set arrays that will store values of height z and velocity v at each time step
    z = np.zeros(1000)
    v = np.zeros(1000)
    # Set the initial values of height z, velocity v and time step ts
    z[0] = h
    ts = 0
    v[0] = 0    
    # Set the iterator
    i = 0
    # Run the system of equations at each time step until Wille-E reaches the ground
    while (z[i] > 0):
        print("At t =", ts, "s, Wille-E's height =", z[i], "m.")
        i = i+1
        ts = ts + dt
        v[i] = v[i-1] - 9.81*dt
        z[i] = z[i-1] + v[i-1]*dt
    print("SLAM to the ground at t =", ts, "s.")
    #Return the arrays of heights and velocities
    return z[:i+1],v[:i+1]
    
    
# Test the function    
z,v = p8_2(1, 100)
plt.plot(0.5*11.5*(v**2), label = "Kinetic energy, J")
plt.plot(11.5*9.81*z, label = "Potential energy, J")
plt.plot(0.5*11.5*(v**2) + 11.5*9.81*z, label = "Total energy, J")
plt.xlabel("Time, s")
plt.title("Energy balance, Problem 8b")
plt.legend()
plt.show()