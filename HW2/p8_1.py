import math

# dt is the time step
# h is height from the ground
# The function will print out Wille-E's height at each time step

def p8_1(dt, h):
    # Set the initial values of height z and time step ts
    z = h
    ts = 0
    # Execute the conditional loop
    while (z > 0):
        z = z - dt * (math.sqrt(2*9.81*(z - h)))
        ts = ts + 1
        print("At time step = ", ts, ": Wille-E's height = ", z)
        # The loop will be going forever, unless we stop it
        if ts >= 50:
            print("Endless loop. Terminating the process.")
            break
        
    
p8_1(1, 16)