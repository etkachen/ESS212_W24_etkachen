# The recursive function for calculating the binomial coefficient
def binom_coeff_rec(n, k):
    # Is k first or last?
    if (k == n or k == 0):
        return 1
    # if not, use formula (7)
    else:
        return binom_coeff_rec(n-1, k-1) + binom_coeff_rec(n-1, k)
        
# The enveloping function 
# Needed to subtract 1 from the initial k to let k go to 0 and avoid the infinite loop
def binom_coeff(n, k):
    k = k-1
    return binom_coeff_rec(n,k)


# Running tests
        
print("Testing the recursive function for calculating the k-th binomial coefficient for the n-th power.")
print("For n = 0, k = 1: C(n,k) = ", binom_coeff(0, 1))
print("For n = 2, k = 3: C(n,k) = ", binom_coeff(2, 3))
print("For n = 3, k = 3: C(n,k) = ", binom_coeff(3, 3))
print("For n = 5, k = 1: C(n,k) = ", binom_coeff(5, 1))
print("For n = 8, k = 7: C(n,k) = ", binom_coeff(8, 7))


# Now that we have the function for calculating binomial coefficients, we can have a function for printing out the entire row of the Pascal triangle.
# We will use the finite loop of n iterations.

def pascal_row(n):
    row = []
    for k in range(1, n+1):
        row.append(binom_coeff(n, k))
        row.append(0)
    row.append(binom_coeff(n, n+1))
    return row
    

# Running tests

print("Testing the function for printing out the nth row of the Pascal triangle.")
print("For n = 0: ", pascal_row(0))
print("For n = 2: ", pascal_row(2))
print("For n = 5: ", pascal_row(5))
print("For n = 8: ", pascal_row(8))
        
