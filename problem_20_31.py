from numpy import matrix
from numpy.linalg import inv


I = matrix([[4, -2, 0],
            [-2, 3, 1],
            [0, 1, 5]])

I_inv = inv(I)
omega = [6, 6, -4]
stor_omega = matrix([[0, -omega[2], omega[1]],
                     [omega[2], 0, -omega[0]],
                     [-omega[1], omega[0], 0]])
omega = matrix(omega)
alpha = I_inv * stor_omega * I * omega.transpose()
print("Angular acceleration alpha is")
print(alpha)
