def B_sqrt(c, tol):
    # since the square root of a negative number is complex and is out of scope of this assignment, we treat cases of negative c as undefined.
    if c < 0:
        return float('NaN')
	# initial guess: if > 100, divide the number by a factor of half of digits in c, otherwise divide by half
    x = 0
    c_len = len(str(c))
    if c_len > 2:
        x = c/(c_len*10)
    else:
        x = c/2
    # execute the Babylonian algorithm
    while abs(x**2 - c) >= tol:
        x = 0.5 * (x + c/x)
    return x
    
def unit_test(c, tol):
    if round(B_sqrt(c, tol), len(str(tol))-1) == round(c**0.5, len(str(tol))-1):
        print("Pass")
    else:
        print("Fail")
    
print("Testing the code for Problem 6.")
print("c = 2, 0.001 precision: ", round(B_sqrt(2, 0.001), 3))
unit_test(2, 0.001)
print("c = 2, 0.000001 precision: ", round(B_sqrt(2, 0.000001), 6))
unit_test(2, 0.000001)
print("c = 81, 0.0001 precision:", round(B_sqrt(81, 0.0001), 4))
unit_test(81, 0.0001)

