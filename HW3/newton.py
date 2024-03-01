import numpy as np
import matplotlib.pyplot as plt

# Function that returns the Jacobian matrix

def jac(a,b,c):
    return [[16 + 4*b + 4*c + b*c, 4*a + a*c, 4*a + a*b],[b*c, a*c, a*b],[16 - 4*b - 4*c + b*c, -4*a + a*c, -4*a + a*b]]

# Function that returns the guess of the beta vector

def func(a,b,c):
    return [16*a+4*a*b+4*a*c+a*b*c-30, a*b*c-2, 16*a-4*a*b-4*a*c+a*b*c-6]

# Newton's method

def newton(beta,imax,tol):
    # Write beta into a local variable, just in case
    b = beta
    for i in range(imax):
        # Calculate Jacobian and the function value
        J = jac(b[0],b[1],b[2])
        F = func(b[0],b[1],b[2])
        # Calculate the solution for the linear matrix equation
        beta_guess = np.linalg.solve(J,F)
        # Take the difference; this is the new guess
        b = b - beta_guess
        # Check if the solution converged
        if np.linalg.norm(beta_guess) < tol: 
            break
    return b
    
    
#Print the result
    
print(newton([1,2, 3],100,1e-5))


# Function that checks if the Newton's method will converge with the given (b,c) point 
# Criterion for Newton's method failing: determinant of Jacobian is 0 or number of max iterations is reached
# Returns 0 if the method fails, 1 otherwise

def newton_check(b,c,imax,tol):
    beta = [1,b,c]
    for j in range(imax):
        J = jac(beta[0], beta[1], beta[2])
        if (np.linalg.det(J)==0) or (j == imax-2):
            return 0
        F = func(beta[0], beta[1], beta[2])
        beta_guess = np.linalg.solve(J,F)
        beta = beta - beta_guess
        if np.linalg.norm(beta_guess) < tol: 
            break
    return 1
    
# array resolution
n = 100
# empty array for the plot
M = np.zeros([n, n])
# arrays of b and c
bval = np.linspace(-10, 10, n)
cval = np.linspace(-10, 10, n)

# run newton_check through all points, form a matrix
for u, x in enumerate(bval):
    for v, y in enumerate(cval):
        M[v, u] = newton_check(x,y,100,1e-5)

#Plot it

plt.imshow(M, cmap=plt.cm.Reds, interpolation='none', extent=[-10,10,-10,10])
plt.colorbar(label='Convergence')
plt.xlabel("b")
plt.ylabel("c")
plt.title("Newton's method convergence plot")

plt.show()

        

