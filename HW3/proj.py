import numpy as np

# Data vector
d = [30,2,6]

#Model matrix
a = [16, 0, 16]
b = [-4, 0, 4]
c = [1, 1, 1]

Am = [a,b,c]

At = np.transpose(Am)

AtAm = np.matmul(At, Am)

Atd = np.matmul(At, d)

AtAmInv = np.linalg.inv(AtAm)

x = np.matmul(AtAmInv, Atd)

print('Solution: ', x)

e = d - np.matmul(Am, x)

print('Error: ', e)