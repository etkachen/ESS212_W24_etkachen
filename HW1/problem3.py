# Defining functions provided in homework PDF 

def S1_rec(n):
	if n > 1:
		S = n + S1_rec(n-1)
	else:
		S = 1
	return S

def S1_iter(n):
	S = 0;
	for i in range(1,n+1):
		S = S+i
	return S
    
# Running tests

print("Testing the functions provided in the Homework 1 PDF for calculating S1.")
print("Recursive function, for n = 5: S = ", S1_rec(5))
print("Iterative function, for n = 5: S = ", S1_iter(5))
# Both functions work.

# Defining functions and running tests for other two equations provided for the Problem 3 

def O1_rec(n):
    if n > 1:
        O = (2*n-1) + O1_rec(n-1)
    else:
        O = 1
    return O
    

print("Testing the recursive function for calculating O1.")
print("For n = 5: O = ", O1_rec(5))
print("For n = 8: O = ", O1_rec(8))


def S2_rec(n):
    if n > 1:
        S = (n**2) + S2_rec(n-1)
    else:
        S = 1
    return S
    

print("Testing the recursive function for calculating S2.")
print("For n = 5: S = ", S2_rec(5))
print("For n = 8: S = ", S2_rec(8))
