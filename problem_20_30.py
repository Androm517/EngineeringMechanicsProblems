from numpy import matrix

I = matrix([[4, -2, 0],
            [-2, 3, 1],
            [0, 1, 5]])
omega = [6, 6, -4]
stor_omega = matrix([[0, -omega[2], omega[1]],
                     [omega[2], 0, -omega[0]],
                     [-omega[1], omega[0], 0]])
omega = matrix(omega)
alpha = matrix([0, 0, 0])

M = I * alpha.transpose() + stor_omega * I * omega.transpose()
print("Total moment M is")
print(M)
