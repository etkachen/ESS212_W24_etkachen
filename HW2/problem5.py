def S_p5(n):
    if n < 0:
        return float('NaN')
    elif n == 0:
        S = 0
    elif n == 1:
        S = 1
    else:
        S = 2*S_p5(n-1) + 2*S_p5(n-2)
    return S
    
print("Testing the code for Problem 5.")
print("n = -4: S = ", S_p5(-4))
print("n = 0: S = ", S_p5(0))
print("n = 1: S = ", S_p5(1))
print("n = 2: S = ", S_p5(2))
print("n = 3: S = ", S_p5(3))
print("n = 4: S = ", S_p5(4))
print("n = 5: S = ", S_p5(5))

def cfs(n):
    S = (1/(3**0.5))*((1+(3**0.5))/2)**n - (1/(3**0.5))*((1-(3**0.5))/2)**n
    return S

print("Testing the closed form solution.")
print("n = 0: S = ", cfs(0))
print("n = 1: S = ", cfs(1))
print("n = 2: S = ", cfs(2))
print("n = 3: S = ", cfs(3))
print("n = 4: S = ", cfs(4))
print("n = 5: S = ", cfs(5))