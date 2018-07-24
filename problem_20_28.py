from numpy import matrix

I = matrix([[0.05, -0.03, 0],
            [-0.03, 0.08, 0],
            [0, 0, 0.04]])
omega_list = [1.2, 0.8, -0.4]
omega = matrix(omega_list)
alpha = matrix([0.26, -0.07, 0.13])
stor_omega = matrix([[0                 , -omega_list[2], omega_list[1]],
                     [omega_list[2] , 0                 , -omega_list[0]],
                     [-omega_list[1], omega_list[0], 0]])
M = I * alpha.transpose() + stor_omega * I * omega.transpose()
print("Total moment M is")
print(M)
