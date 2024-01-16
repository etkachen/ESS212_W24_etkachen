# A function for calculating the sum of the geometric progression using Equation (19) from the Homework 1 PDF.
# a is the initial value, n is the number of elements in the progression, r is the rate of multiplication.

def geom_prog_sum(a, n, r):
    # If r is not equal to 1, just use the Equation (19)
    if r != 1:
        return (a * (1 - r**n))/(1 - r)
    else:
        return a*n
        
print("Testing the function for calculating the sum of the geometric progression.")
print("For a = 1, n = 5, r = -0.5: S = ", geom_prog_sum(1, 5, -0.5))
print("For a = 2, n = 5, r = 0: S = ", geom_prog_sum(2, 5, 0))
print("For a = 1, n = 5, r = 0.4: S = ", geom_prog_sum(1, 5, 0.4))
print("For a = 2, n = 5, r = 1: S = ", geom_prog_sum(3, 5, 1))
print("For a = 2, n = 5, r = 2: S = ", geom_prog_sum(3, 5, 2))
        